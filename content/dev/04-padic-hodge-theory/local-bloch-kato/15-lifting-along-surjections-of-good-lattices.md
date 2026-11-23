---
title: Lifting along surjections of good lattices
decls:
  - GlobalTheory.TheoremT.liftF_of_isGood
  - GlobalTheory.T.lift_surjection_good_crystalline_lattices
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Lifting along surjections of good lattices

This section proves the main estimate of Theorem T. Let $g : T_1 \to T_2$ be a surjection of good lattices of $G_{\mathbb{Q}_\ell}$. Then every finite cocycle of $T_2$, times an explicit power of $\ell$, is the image of a finite cocycle of $T_1$ up to a coboundary. The proof moves the problem to the Breuil-Kisin packs of [the previous section](/entry/exists-pack-is-of-type/), solves it there with the lifting theorem for $\varphi$-modules, and moves the solution back. The estimate is used in the next section, where the tame field is chosen and Theorem T is proved.

We keep the notation of the previous section. For a lattice $T$ we write $Z^1_f(T)$ for its finite cocycles and $B^1(T)$ for its coboundaries, as in Section 7. Recall from that section that a lattice map $g : T_1 \to T_2$ *lifts with exponent* $s$ if
$$\ell^s\, Z^1_f(T_2) \subseteq g_* Z^1_f(T_1) + B^1(T_2).$$

**Definition 7.15.1 (Numerical conditions).** Let $\ell$ be a prime, $e \ge 1$, $N, \eta, H \ge 0$, $\Sigma \subseteq \mathbb{Z}/e$ and $U \subseteq \mathbb{Z}$ finite. The *numerical conditions* for $(\ell, e, N, \eta, H, \Sigma, U)$ are:

1. $\ell c \in \Sigma$ for every $c \in \Sigma$, and $0 \in \Sigma$;
2. $|\Sigma| \le N$ and $N \ge 2$;
3. $-\eta \le i \le H$ for every $i \in U$, $0 \in U$, and $|U| \le N + 1$;
4. $1 \le \eta < H$;
5. $40(H N^2 + N^3) < \ell$.

The *period* $r(\Sigma)$ is the largest, over $c, c' \in \Sigma$, of the least period of $c - c'$ under $x \mapsto \ell x$ on $\mathbb{Z}/e$.

The period $r(\Sigma)$ measures how far the tame characters $\omega^c$, $c \in \Sigma$, are from being fixed by Frobenius. For example, if $\Sigma = \{0\}$, then $r(\Sigma) = 1$.

To state the steps of the proof we use three notions attached to a Breuil-Kisin datum $D$ with $\varphi$-module $P$, which we do not unfold. The *monodromy class* of a vector $y$ is the class of $E N y - E \zeta(y)$ modulo $M_R$, for a correction term $\zeta(y)$. A cocycle $c$ of $T$ is a *Galois class* of $y$ for a Galois datum $(j, j_B)$ if $c(g) = g b - b$ for a period $b \in B_{\mathcal{O}} \otimes T$ built from two solutions: a solution $m_0$ over $W_{\mathcal{O}}$ of $\varphi(m_0) - m_0 = y$, and a solution $\sigma$, invariant under the descent datum, of $N \sigma = \zeta(y)$, where $N = X \nabla_P$. Two Galois classes of the same vector differ by a coboundary, and the Galois classes are compatible with maps of packs.

**Theorem 7.15.2 (Lifting along surjections of good lattices).** Assume the theorem of Bhatt and Scholze on crystalline lattices and the theorem of Fontaine. Let $\ell$ be a prime, $e + 1 = \ell^a$, $\varpi$ a system of roots, and $L$ a finite extension of $\mathbb{Q}_\ell$ that contains the unramified field of degree $a$, with tame descent data. Fix standard period data for $\mathbb{Q}_\ell$. Let $N, \eta, H, \Sigma, U$ satisfy the numerical conditions, and put $r = r(\Sigma)$. Let $g : T_1 \to T_2$ be a map of $\mathcal{O}$-lattices of $G_{\mathbb{Q}_\ell}$ that is onto, with $T_1$ and $T_2$ good for $(\Sigma, U)$. Then $g$ lifts with exponent
$$7\big(N r + \eta (N + r)\big).$$

Lean: `GlobalTheory.TheoremT.liftF_of_isGood` (also `GlobalTheory.T.lift_surjection_good_crystalline_lattices`, a second name).

*Proof.* Put $\epsilon = 2(N - 1) r$, $c_1 = \eta(r + 1)$, $c_2 = c_1 + \epsilon$ and
$$k = c_2 + \eta + (N + 1)\eta + \epsilon.$$
From $N \ge 2$ and $40(HN^2 + N^3) < \ell$ we get $\ell \ne 2$ and $8H + 1 < \ell$.

*Step 1: the kernel.* The kernel $T_0$ of $g$ is a good lattice for $(\Sigma, U)$, and $0 \to T_0 \xrightarrow{f} T_1 \xrightarrow{g} T_2 \to 0$ is exact. This uses the theorem of Fontaine.

*Step 2: packs.* By [the theorem on packs](/entry/exists-pack-is-of-type/), each $T_i$ has a pack $P_i$ of heights $(\eta, H)$, and $P_1$ and $P_2$ are of type $(\Sigma, U)$. The condition $U \subseteq [-\eta, H]$ is part 3 of the numerical conditions. By the second part of the theorem of Bhatt and Scholze, $f$ and $g$ lift to maps of Breuil-Kisin data $F : P_0 \to P_1$ and $G : P_1 \to P_2$ that respect the descent data. Since the sequence of lattices is exact, so is $P_0 \to P_1 \to P_2$.

*Step 3: a vector for $c$.* Let $c \in Z^1_f(T_2)$. Since $T_2$ is good, there is a vector $y_2$ of $P_2$ with monodromy class $0$ that has $\ell^\epsilon c$ as a Galois class. By the descent datum, $\ell^\eta y_2 = y_2' + (\varphi(m_2) - m_2)$ with $y_2'$ and $m_2$ in the lattices of the lifting theorem. The monodromy class of $\varphi(m_2) - m_2$ is minus the class of $E N m_2$, which is $0$ since $E N(M) \subseteq M_R$. So $y_2' + \varphi(m_2)$ has monodromy class $0$, and, since adding $\varphi(m_2) - m_2$ does not change Galois classes, it has $\ell^{\eta + \epsilon} c$ as a Galois class.

*Step 4: lifting in the $\varphi$-modules.* The hypotheses of [the lifting theorem for $\varphi$-modules](/entry/lifting-theorem-phi-modules-exact-triple/) hold: the triple is exact, the numerical conditions hold, $P_1$ is of type $(\Sigma, U)$, and the characters of $P_2$ lie in $\Sigma$. So there are $y'$ and $m$ in $P_1$ such that $y' + \varphi(m)$ has monodromy class $0$ and
$$G\big(y' + \varphi(m)\big) = \ell^{k} \big(y_2' + \varphi(m_2)\big).$$

*Step 5: back to Galois cocycles.* Since $8H + 1 < \ell$ and $\eta < H$, the correction term $\ell^{c_1} \zeta(y' + \varphi(m))$ is integral. By [the theorem on Galois classes](/entry/galois-class-of-monodromy-eq-zero/), there is $\kappa_1 \in Z^1_f(T_1)$ that is a Galois class of $\ell^{c_1}(y' + \varphi(m))$. This uses the theorem of Fontaine.

*Step 6: comparison.* Galois classes are compatible with $G$ and $g$, so $g_* \kappa_1$ is a Galois class of $G(\ell^{c_1}(y' + \varphi(m))) = \ell^{c_1 + k}(y_2' + \varphi(m_2))$. By Step 3, $\ell^{s} c$ is also a Galois class of this vector, where
$$s = c_1 + k + \eta + \epsilon.$$
Two Galois classes of one vector differ by a coboundary. So $\ell^{s} c = g_* \kappa_1 - \beta$ with $\beta \in B^1(T_2)$.

*Step 7: the exponent.* We compute
$$\begin{aligned} s &= 2\eta(r + 1) + 3\epsilon + (N + 3)\eta \\ &= 2\eta r + (N + 5)\eta + 6(N - 1) r. \end{aligned}$$
With $N \ge 2$, write $N = n + 2$. Then $7(Nr + \eta(N + r)) - s = (n + 8) r + 6 n \eta + 4 \eta + 5 \eta r$, which is $\ge 0$. So $s \le 7(Nr + \eta(N + r))$. Multiply the relation of Step 6 by $\ell^{7(Nr + \eta(N + r)) - s}$. The result is $\ell^{7(Nr + \eta(N + r))} c = g_*(\ell^{\cdots} \kappa_1) - \ell^{\cdots}\beta$, which lies in $g_* Z^1_f(T_1) + B^1(T_2)$. $\square$

The bound $H$ does not appear in the exponent: it enters only through the condition $8H + 1 < \ell$ of Step 5 and through the heights of the packs.

**Remark 7.15.3 (Formalization).** The steps are lemmas imported from "Statement" files: `isGoodLattice_kernel_of_surjection_goodLattice` (Step 1), `latticeHom_lifts_breuilKisinDescentHom` and `isExactTriple_breuilKisin_of_shortExactLattices` (Step 2), `crystalline_class_from_monodromy_kernel_element`, `prime_pow_divisibility_of_descentDatum` and `exists_frobeniusPotential_cocycle_class` (Step 3), `zeta_mem_pow_inv_phiModule_lattice` (Step 5) and `tame_breuil_kisin_datum_exists` (Step 6). We read their uses, not their proofs, and we did not unfold the monodromy class, the correction term $\zeta$ or the Galois classes; the description of these notions above follows the definitions `Mon`, `IsPotential` and `ClassOf`. The proof sets `maxHeartbeats` to 4000000 and `synthInstance.maxHeartbeats` to 400000 ([LiftSurjectionGoodCrystallineLattices.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LiftSurjectionGoodCrystallineLattices.lean#L24)). The numerical conditions exist twice, as `Numerics` and as `Admissible`, two structures with the same ten fields ([ConductorExponents.lean](lean:Development/AbelianVarietyTheory/BlockTheory/NonGaloisCusps/ConductorExponents.lean#L20) and [AdmissibleSignatures.lean](lean:Development/AbelianVarietyTheory/BlockTheory/NonGaloisCusps/AdmissibleSignatures.lean#L10)), and lines 45 to 47 copy one into the other. The type of the pack of $T_0$ is discarded (line 38). The second name is a one-line wrapper.
