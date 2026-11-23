---
title: The Frobenius factorisation
decls:
  - CrystallineSemistableComparison.Pb.pin_all
  - CrystallineSemistableComparison.Pb.fac_ex
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Frobenius factorisation

This section proves the Frobenius factorisation. For a smooth model $\mathfrak{X}$, it compares the second crystalline family $H'^j(\mathfrak{X})$ of section 5 over $A_{\mathrm{cris}}$ with $A_{\mathrm{cris}} \otimes_{W(k)} L^j$, where $L^j$ is the crystalline cohomology of $\mathfrak{X}$ over $W(k)$. There are maps $\alpha$ and $\beta$ between them with $\beta \alpha = \ell^e \phi^N$, and $\alpha$ respects Frobenius, the action of $G_K$ and pullbacks. This is the Frobenius map of part 4 of the theorem on the data for the crystalline comparison ([Theorem 2.5.7](/entry/p-seam/)). The proof uses the level sequences of the last section ([Theorem 2.11.6](/entry/ls-seq/)) and finite length at level one ([Theorem 2.10.4](/entry/smooth-model-finite-length-link/)).

We keep the notation of the last two sections. So $(k, \rho, s)$ is a residue datum and $w : W(k) \to A_{\mathrm{cris}}$ is the map that it gives. Let $\phi$ be the Frobenius of $A_{\mathrm{cris}}$ and $F$ the Frobenius of $W(k)$. For a model $\mathfrak{X}$, $j \geq 0$ and $n \geq 1$ we use three systems.

1. $H'_n$ is the crystalline cohomology of $\mathfrak{X}$ over $A_{\mathrm{cris}}/\ell^n$ along the standard map $\kappa_b$ from $\mathcal{O}_K$ to $A_{\mathrm{cris}}/\ell^n$ modulo its divided power ideal. Its limit is $H'^j(\mathfrak{X})$, with the Frobenius $\phi_H$, the action of $G_K$ and pullbacks.
2. $T_n$ is the crystalline cohomology of $\mathfrak{X}$ over $A_{\mathrm{cris}}/\ell^n$ along the map $\kappa_m$ that goes through the residue field: $\mathcal{O}_K \xrightarrow{\rho} k$, followed by the map that $w$ induces.
3. $S_n = H^j_n(\mathfrak{X})$ over $W_n(k)$, as in the last section, with limit $L^j = \varprojlim_n S_n$ and Frobenius $\phi_L$.

Base change along $w$ gives $w$-semilinear maps $g_n : S_n \to T_n$ that commute with the transitions. Let $E_n : A_{\mathrm{cris}} \otimes_{W(k)} L^j \to T_n$ be the additive map with $E_n(a \otimes y) = a\, g_n(y_n)$.

**Definition 2.12.1 (Teichmüller congruence).** Let $N \geq 0$. The residue datum satisfies the *Teichmüller congruence for $N$* if $\phi^N \circ \kappa_b = \kappa_m$ as maps from $\mathcal{O}_K$ to $A_{\mathrm{cris}}/\ell^n$ modulo its divided power ideal, for every $n$.

On that quotient, $\phi^N$ is $q \mapsto q^{\ell^N}$. The usual reason for the congruence at large $N$ is that the two images of $x \in \mathcal{O}_K$ differ by an element that the condition on $s$ makes small, and raising to a large power of $\ell$ kills the difference. So the congruence says that $\phi^N$ moves the standard base to the base through the residue field. Under the congruence, pull back along $\phi^N$ gives $\phi^N$-semilinear maps $\nu_n : H'_n \to T_n$, and a map of sites in the other direction gives $A_{\mathrm{cris}}$-linear maps $\mu_n : T_n \to H'_n$. Both families commute with the transitions.

**Definition 2.12.2 (Pinned map).** Let $e \geq 0$ and $\alpha : H'^j(\mathfrak{X}) \to A_{\mathrm{cris}} \otimes_{W(k)} L^j$ be additive. The pair $(e, \alpha)$ *pins* $\nu$ if:

1. *separation:* if $E_n(z) = 0$ for all $n$, then $z = 0$;
2. *pinning:* $E_n(\alpha(x)) = \ell^e \nu_n(x_n)$ for all $n$ and all $x \in H'^j(\mathfrak{X})$.

So $\alpha$ is a lift of $\ell^e \nu$ through the maps $E_n$. If $A_{\mathrm{cris}} \otimes L^j \to \varprojlim T_n$ were bijective, one could take $e = 0$ and $\alpha$ the inverse map applied to $\nu$. In general the tensor product does not commute with the limit, and the power $\ell^e$ measures the defect.

**Lemma 2.12.3 (Existence of a pinned map).** Let $W$ be a discrete valuation ring in which $\ell$ is irreducible, and $c \geq 0$. Let $S$ be a system of $W$-modules such that $\varprojlim S$ is a finite $W$-module, $\ell^n$ kills $S_n$, every $x \in \varprojlim S$ with $x_n = 0$ is $\ell^n y$ for some $y \in \varprojlim S$, and for every $x \in S_n$ there is $y \in \varprojlim S$ with $y_n = \ell^c x$. Let $A$ be a flat $W$-algebra that is $\ell$-adically complete. Let $T$ be a system of $A$-modules and $g : S \to T$ a map of systems, semilinear along $W \to A$, such that $a \otimes y \mapsto a\, g_n(y)$ is a bijection $A \otimes_W S_n \to T_n$ for each $n$. Then for every system $H$ of $A$-modules and every map of systems $\nu : H \to T$, semilinear along a ring map of $A$, there is an additive $\alpha : \varprojlim H \to A \otimes_W \varprojlim S$ such that $(c, \alpha)$ pins $\nu$.

Lean: `CrystallineSemistableComparison.Pb.Fa.pin_ex`.

*Proof.* We take as given, from the theory of finite modules over a discrete valuation ring, that under these hypotheses the map $A \otimes_W \varprojlim S \to \varprojlim_n (A \otimes_W S_n)$ is injective, and that there is a map $\alpha'$ back with $\alpha'(u)_n = \ell^c u_n$ in $A \otimes_W S_n$. Through the bijections $A \otimes_W S_n \cong T_n$, injectivity is separation. Let $x \in \varprojlim H$. The family $(\nu_n(x_n))_n$ is compatible, so its preimages $u_n \in A \otimes_W S_n$ are compatible too, and $z = \alpha'(u)$ satisfies $E_n(z) = \ell^c \nu_n(x_n)$ for all $n$. By separation $z$ is unique. Let $\alpha(x) = z$. For $x$ and $x'$, the element $\alpha(x + x') - \alpha(x) - \alpha(x')$ has all $E_n$ equal to zero, so $\alpha$ is additive. $\square$

**Theorem 2.12.4 (Pinned maps for all models).** Let $(k, \rho, s)$ be a residue datum that satisfies the Teichmüller congruence for $N$. For every model $\mathfrak{X}$ and every $j \geq 0$ there are $e \geq 0$ and an additive map $\alpha : H'^j(\mathfrak{X}) \to A_{\mathrm{cris}} \otimes_{W(k)} L^j$ such that, if $\mathfrak{X}$ is smooth, then $(e, \alpha)$ pins $\nu$.

Lean: `CrystallineSemistableComparison.Pb.pin_all`.

*Proof.* If $\mathfrak{X}$ is not smooth, take $e = 0$ and $\alpha = 0$; there is nothing to prove. Let $\mathfrak{X}$ be smooth. We check the hypotheses of the lemma with $W = W(k)$, $A = A_{\mathrm{cris}}$ and $S_n = H^j_n(\mathfrak{X})$. Take a level sequence for $(H^j_n, H^{j+1}_n)$ from the last section. We take as given four facts on systems with a level sequence whose first level has finite length, which holds here by section 10:

1. every $S_n$ has finite length, so it is artinian;
2. the limit $\varprojlim S$ is a finite $W(k)$-module, and the same holds in degree $j + 1$;
3. there is $c$ such that for every $x \in S_n$ some $y \in \varprojlim S$ has $y_n = \ell^c x$;
4. every $x \in \varprojlim S$ with $x_n = 0$ is $\ell^n y$ for some $y$.

The ring $W(k)$ is a discrete valuation ring with uniformizer $\ell$. We take as given that $A_{\mathrm{cris}}$ is flat over $W(k)$ and $\ell$-adically complete, and that for a smooth model the base change map $A_{\mathrm{cris}} \otimes_{W(k)} S_n \to T_n$ is bijective. The lemma gives $\alpha$ with $e = c$. $\square$

**Definition 2.12.5 (Frobenius factorisation).** Let $N \geq 0$. A *Frobenius factorisation* for $N$ assigns to each model $\mathfrak{X}$ and $j \geq 0$ an integer $e = e(\mathfrak{X}, j) \geq 0$, an additive map $\alpha_{\mathfrak{X}}$ and an $A_{\mathrm{cris}}$-linear map $\beta_{\mathfrak{X}}$
$$H'^j(\mathfrak{X}) \xrightarrow{\ \alpha\ } A_{\mathrm{cris}} \otimes_{W(k)} L^j \xrightarrow{\ \beta\ } H'^j(\mathfrak{X}),$$
and additive maps $\phi_T$ and $g_T$ (for $g \in G_K$) on $A_{\mathrm{cris}} \otimes L^j$, such that for all smooth $\mathfrak{X}$, all $j$, $a \in A_{\mathrm{cris}}$, $x \in H'^j(\mathfrak{X})$, $y \in L^j$ and $g \in G_K$:

1. $\phi_T(a \otimes y) = \phi(a) \otimes \phi_L(y)$ and $g_T(a \otimes y) = g(a) \otimes y$;
2. $\alpha(a x) = \phi^N(a)\, \alpha(x)$;
3. $\beta(\alpha(x)) = \ell^e \phi_H^N(x)$;
4. $\alpha(\phi_H x) = \phi_T(\alpha(x))$ and $\alpha(g x) = g_T(\alpha(x))$;
5. $g(\beta(1 \otimes y)) = \beta(1 \otimes y)$;
6. for a map $u : \mathfrak{X} \to \mathfrak{X}'$ of smooth models over $\mathcal{O}_K$ and $x \in H'^j(\mathfrak{X}')$, there is $m \geq 0$ with
$$\ell^m \Big(\ell^{e(\mathfrak{X}', j)}\, \alpha_{\mathfrak{X}}(u^* x) - \ell^{e(\mathfrak{X}, j)}\, (1 \otimes u^*)\big(\alpha_{\mathfrak{X}'}(x)\big)\Big) = 0.$$

The factorisation is *pinned* if for every smooth $\mathfrak{X}$ and every $j$, $(e, \alpha)$ pins $\nu$ and $\beta(z) = (\mu_n(E_n(z)))_n$ for all $z$.

Conditions 2 and 3 say that, up to $\ell^e$, the $N$-th power of the crystalline Frobenius factors through the tensor product. Conditions 1, 4 and 5 make the factorisation compatible with the Frobenius and Galois structures on both sides, and condition 6 makes it natural up to torsion.

**Theorem 2.12.6 (Existence of a Frobenius factorisation).** Let $(k, \rho, s)$ be a residue datum that satisfies the Teichmüller congruence for $N$. Assume:

1. $\mu_n(\nu_n(x)) = \phi_H^N(x)$ for every model $\mathfrak{X}$, all $n$, $j$ and $x \in H'_n$;
2. $\phi(w(a)) = w(F(a))$ for all $a \in W(k)$;
3. $g(w(a)) = w(a)$ for all $g \in G_K$ and $a \in W(k)$.

Then there is a pinned Frobenius factorisation for $N$.

Lean: `CrystallineSemistableComparison.Pb.fac_ex`.

*Proof.* For each $\mathfrak{X}$ and $j$ choose $e$ and $\alpha$ by the last theorem. Let $\beta(z) = (\mu_n(E_n(z)))_n$. This is $A_{\mathrm{cris}}$-linear, since $E_n$ and $\mu_n$ are. By hypothesis 2, $a \otimes y \mapsto \phi(a) \otimes \phi_L(y)$ is well defined on the tensor product over $W(k)$; let $\phi_T$ be this map. By hypothesis 3, $g_T(a \otimes y) = g(a) \otimes y$ is well defined. This gives condition 1. Let $\mathfrak{X}$ be smooth. Each remaining condition is an equation in $A_{\mathrm{cris}} \otimes L^j$, so by separation it suffices to compare the images under every $E_n$.

1. *Condition 2.* $E_n(\alpha(ax)) = \ell^e \nu_n(a x_n) = \ell^e \phi^N(a) \nu_n(x_n) = E_n(\phi^N(a) \alpha(x))$, since $\nu_n$ is $\phi^N$-semilinear and $E_n$ is $A_{\mathrm{cris}}$-linear.
2. *Condition 3.* $\beta(\alpha(x))_n = \mu_n(\ell^e \nu_n(x_n)) = \ell^e \phi_H^N(x_n)$ by hypothesis 1.
3. *Condition 4.* The maps $\nu_n$ and $g_n$ commute with Frobenius and with $G_K$. So $E_n(\alpha(\phi_H x)) = \ell^e \nu_n(\phi_H x_n)$ and $E_n(\phi_T \alpha(x)) = \phi(E_n(\alpha(x))) = \ell^e \phi(\nu_n(x_n))$ agree, and the same holds for $g$.
4. *Condition 5.* $\beta(1 \otimes y)_n = \mu_n(g_n(y_n))$. Here $g_n(y_n)$ is fixed by $G_K$ because of hypothesis 3, and $\mu_n$ commutes with $G_K$.
5. *Condition 6, with $m = 0$.* The maps $\nu_n$ and $g_n$ commute with $u^*$. So the images under $E_n$ of $\ell^{e'} \alpha_{\mathfrak{X}}(u^* x)$ and of $\ell^{e} (1 \otimes u^*)(\alpha_{\mathfrak{X}'}(x))$ are both $\ell^{e + e'} \nu_n(u^* x_n)$, with $e = e(\mathfrak{X}, j)$ and $e' = e(\mathfrak{X}', j)$.

The factorisation is pinned by the choice of $\alpha$ and the definition of $\beta$. $\square$

The hypotheses hold. The Teichmüller congruence holds for some $N$, hypothesis 1 holds by the construction of $\mu_n$ and $\nu_n$, and hypotheses 2 and 3 are properties of $w$. With these, part 4 of [Theorem 2.5.7](/entry/p-seam/) is proved.

**Remark 2.12.7 (Formalization).** Both theorems are in [PhiAIter.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/FrobeniusFactorisation/PhiAIter.lean#L44); the file name describes only the helper `phiA_iter`. The lemma is `Fa.pin_ex` and the pinned condition is `Fa.Pin` in ExistsAlpha.lean, and the factorisation is `Fac` in PhiTTmul.lean. The maps $\nu_n$ and $\mu_n$ are `Mid.nu` and `Mid.mu` in MuMor.lean, and the congruence is `Mid.TeichmullerCongruence`; we did not unfold the morphisms of sites behind $\nu_n$ and $\mu_n$ or the proof of `teich`, so the description of $\nu_n$, $\mu_n$ and of the reason for the congruence is a reading of types, not of proofs. The facts we take as given are the `GlobalTheory.T` statements `flat_base_change_limit_system`, `finite_length_of_lseq_first`, `module_finite_limit_of_lseq`, `bounded_cokernel_limit_to_level`, `limit_divisible_of_vanishing_level` and `smooth_model_tensor_witt_comparison`, with proofs in `Development/AutomorphicSpectrum/Proofs/BlockDecomposition`, which we did not open. The theorem `pin_all` gives $e = 0$ and $\alpha = 0$ for models that are not smooth, so its conclusion says nothing for them. The naturality condition 6 has an extra factor $\ell^m$, but the proof always takes $m = 0$. The theorem `fac_ex` is used in `fmap` in Pull.lean, where its hypotheses come from `teich`, `Mid.mu_nu`, `w_phi` and `w_fix`, and in PinFixed.lean.

## Notes and references

The results of this chapter feed the geometric steps ([Theorem 3.2 of Volume 9](/entry/steps-holds/)), the crystalline step ([Theorem 3.3 of Volume 9](/entry/crys-step-holds/)) and the Frobenius step ([Theorem 3.10 of Volume 3](/entry/phi-step/)) of the chapter on Galois representations. The data for the crystalline comparison ([Theorem 2.5.7](/entry/p-seam/)) collect the period map ([Theorem 2.5.6](/entry/pmap/)), the local comparison ([Theorem 2.6.9](/entry/local-of/)), the top power of the first Chern class ([Theorem 2.2.4](/entry/pow-k-ne-zero/)) and the Frobenius factorisation of this section. Through these the chapter enters the step [GeoOne holds](/step/geo-one-holds/) of [the Galois row](/proof/galois-row/).

- G. Faltings, "p-adic Hodge theory", *J. Amer. Math. Soc.* 1 (1988). The Hodge-Tate decomposition of the étale cohomology of a proper smooth variety, which sections 3 and 4 prove for smooth projective models.
- G. Faltings, "Crystalline cohomology and p-adic Galois representations", in *Algebraic Analysis, Geometry, and Number Theory*, Johns Hopkins University Press, 1989. The crystalline comparison, of which sections 5 to 12 give the parts that the Galois row uses.
- J.-M. Fontaine, "Le corps des périodes p-adiques", *Astérisque* 223 (1994). The rings $A_{\mathrm{cris}}$, $B_{\mathrm{dR}}^+$ and $B_{\mathrm{dR}}$ and the element $t$.
- J.-M. Fontaine and W. Messing, "p-adic periods and p-adic étale cohomology", *Contemp. Math.* 67 (1987). The Frobenius on crystalline cohomology over $A_{\mathrm{cris}}$ and its comparison with the cohomology of the special fibre.
- B. Bhatt, M. Morrow and P. Scholze, "Integral p-adic Hodge theory", *Publ. Math. IHÉS* 128 (2018). The comparison through perfectoid algebras, with the element $\mu = [\varepsilon] - 1$, which sections 6 to 8 follow.
- P. Berthelot, *Cohomologie cristalline des schémas de caractéristique $p > 0$*, Lecture Notes in Math. 407, Springer, 1974; P. Berthelot and A. Ogus, *Notes on Crystalline Cohomology*, Princeton University Press, 1978. Crystalline cohomology over $W_n(k)$, its finiteness and its base change, used in sections 10 to 12.
- O. Gabber and L. Ramero, *Almost Ring Theory*, Lecture Notes in Math. 1800, Springer, 2003. Statements that hold up to an ideal of small elements, the model for the statements "up to $s$" of sections 6 to 8.
- R. Hartshorne, *Algebraic Geometry*, Springer, 1977. Theorem III.4.5 (Čech cohomology computes sheaf cohomology), Theorem III.3.5 (vanishing on affine schemes) and Theorem III.5.2 (finiteness for projective schemes).
- M. F. Atiyah and I. G. Macdonald, *Introduction to Commutative Algebra*, Addison-Wesley, 1969. Chapter 6 (modules of finite length).

The treatment here differs from these sources in five ways. First, the cohomology groups are cohomology groups of sites of divided power thickenings or of perfect algebras, computed by Čech complexes on a finite cover by charts, and not the cohomology of a sheaf on a scheme. For example, the vanishing of the graded pieces on an affine open is proved for the thickening site directly, where the classical proof identifies $H^j(\mathrm{gr}^r)$ with $H^{j-r}(V, \Omega^r)$ and uses Theorem III.3.5 of Hartshorne. Second, the comparisons of sections 6 to 8 hold up to explicit elements, bounded powers of $\mu$ or Teichmüller lifts $[r_k]$ of roots of $\pi$, and not as almost isomorphisms. Third, $B_{\mathrm{dR}}^+$ enters only through its truncations $B_{\mathrm{dR}}^+/t^m$, with subrings generated by the image of $A_{\mathrm{inf}}$ and divided powers of $\xi/\ell^M$, and the period map is built level by level. Fourth, the long exact sequences for $0 \to W_a(k) \to W_c(k) \to W_b(k) \to 0$ are used only through two of their exactness conditions. Fifth, the crystalline base change of Berthelot and Ogus is used only at each finite level $n$, as $A_{\mathrm{cris}} \otimes_{W(k)} H^j_n \cong T_n$. In the limit, an isomorphism $A_{\mathrm{cris}} \otimes_{W(k)} L^j \cong H'^j(\mathfrak{X})$ is replaced by a factorisation of $\ell^e \phi^N$ through the tensor product.
