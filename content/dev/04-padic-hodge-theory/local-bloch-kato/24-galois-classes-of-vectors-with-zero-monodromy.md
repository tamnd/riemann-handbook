---
title: Galois classes of vectors with zero monodromy
decls:
  - GlobalTheory.BKGal.MonZero.step_mul
  - GlobalTheory.BKGal.MonZero.exists_cob
  - GlobalTheory.BKGal.classOf_of_mon_eq_zero
  - GlobalTheory.T.galoisClass_of_monodromy_eq_zero
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Galois classes of vectors with zero monodromy

This section proves that a vector $y$ of a Breuil-Kisin datum with monodromy class $0$ gives a crystalline cocycle of the Galois lattice $T$. More precisely, if $\ell^c \zeta(y)$ is integral, then $\ell^c y$ has a Galois class in $Z^1_f(T)$. The proof splits $G_{\mathbb{Q}_\ell}$ into the Galois group of the tame field and the Galois group of the Kummer tower, and bounds the coboundary of a potential on each part. The theorem is Step 5 of the proof of [the theorem on lifting along surjections](/entry/lift-f-of-is-good/): it carries the vector found by [the lifting theorem for $\varphi$-modules](/entry/lifting-theorem-phi-modules-exact-triple/) back to Galois cohomology.

We keep the notation of [the previous section](/entry/gb-sub-b-mem-fil-zero/): $D$ is a Breuil-Kisin datum of heights $(\eta, H)$, $T$ is an $\mathcal{O}$-lattice of $G_{\mathbb{Q}_\ell}$ in the representation $V$, $(j, j_B)$ is a Galois datum for $(D, T)$, and potentials, $\zeta$ and $\mathrm{Mon}$ are as defined there. Let $K_\infty = \mathbb{Q}_\ell(\varpi_n^e : n \ge 0)$. Since $\varpi_0^e = -\ell$ and $\varpi_{n+1}^\ell = \varpi_n$, the element $\varpi_n^e$ is an $\ell^n$-th root of $-\ell$, so $K_\infty$ is the Kummer tower of $-\ell$. We write $G_{K_\infty}$ and $G_{K_\varpi}$ for the subgroups of $G_{\mathbb{Q}_\ell}$ that fix $K_\infty$ and the tame field.

**Definition 7.24.1 (Coboundary of a period).** Let $b \in B_{\mathcal{O}} \otimes T$ and let $\kappa : G_{\mathbb{Q}_\ell} \to V$ be a function. We say that $\kappa$ is the *coboundary* of $b$ if for every $g$, every $n \ge 0$ and every $x \in T$ with $x = \ell^n \kappa(g)$, we have
$$1 \otimes x = \ell^n (g b - b).$$

This is the equation $\kappa(g) = g b - b$, written without dividing by $\ell$ inside $B_{\mathcal{O}} \otimes T$. Since $T$ spans $V$, every value $\kappa(g)$ has a multiple $\ell^n \kappa(g)$ in $T$, so the condition is not empty.

**Definition 7.24.2 (Galois class).** A function $\kappa : G_{\mathbb{Q}_\ell} \to V$ is a *Galois class* of a vector $y$ if $\kappa$ is the coboundary of a potential of $y$.

Let $Z^1_f(T)$ be the set of continuous cocycles $\kappa$ of $G_{\mathbb{Q}_\ell}$ with values in $T$ that are crystalline: there is $z \in V \otimes_{\mathbb{Q}_\ell} B_{\mathrm{cris}}$ with $\kappa(g) \otimes 1 = g z - z$ for all $g$. This is the module of finite cocycles of [the section on lifting](/entry/lift-f-of-is-good/), for standard period data.

We take the following results as given. They are proved in other parts of the development, and we read their statements, not their proofs.

**Theorem 7.24.3 (Potentials and classes).** Let $D$, $T$ and $(j, j_B)$ be as above. Then:

1. every $y \in Y_\eta$ has a potential;
2. two Galois classes of the same vector differ by a coboundary $g \mapsto g x - x$ with $x \in T$;
3. if $\kappa$ is a Galois class of $y$, then $\ell^k \kappa$ is a Galois class of $\ell^k y$ for every $k \ge 0$;
4. if $\kappa$ is a Galois class of $y$ and $m \in M^\Delta$, then $\kappa$ is a Galois class of $y + \varphi(m) - m$.

**Theorem 7.24.4 (The Kummer tower).** Let $y \in Y_\eta$, let $b$ be a potential of $y$, and let $k \in G_{K_\infty}$. Then $k b - b = 1 \otimes x$ for some $x \in T$.

**Theorem 7.24.5 (Lowering the exponent).** Let $\eta < H$ and $8 H + 1 < \ell$. Let $y \in Y_\eta$ and $c \ge 0$ with $\ell^c \zeta(y) \in \mathcal{M}$, let $b$ be a potential of $y$, and let $h \in G_{K_\varpi}$. If $\ell^n (h b - b) \in 1 \otimes T$ for some $n \ge 0$, then $\ell^c (h b - b) \in 1 \otimes T$.

**Theorem 7.24.6 (Decomposition).** Let $L$ contain the unramified extension of degree $a$, with tame descent data. Every $g \in G_{\mathbb{Q}_\ell}$ is a product $g = h k$ with $h \in G_{K_\varpi}$ and $k \in G_{K_\infty}$.

The same input theorem lists six more properties of the tame Galois group and of $G_{K_\infty}$, which we do not use.

**Theorem 7.24.7 (Continuity).** Let $\ell \ne 2$, let $T$ be a lattice of $G_{\mathbb{Q}_\ell}$ over the ring of integers of $L$, and let $\kappa$ be the coboundary of some $b \in B_{\mathcal{O}} \otimes T$. Then $\kappa$ is a continuous cocycle.

**Theorem 7.24.8 (Comparison of period rings).** Fix standard period data for $\mathbb{Q}_\ell$, with crystalline ring $B$. There is an $\mathcal{O}$-linear isomorphism $\beta : B_{\mathcal{O}} \otimes T \to V \otimes_{\mathbb{Q}_\ell} B$ with $\beta(1 \otimes x) = x \otimes 1$, which commutes with the Galois actions and with Frobenius. Also, a continuous cocycle $\kappa$ is crystalline if and only if it is the coboundary of some $b \in B_{\mathcal{O}} \otimes T$.

**Lemma 7.24.9 (One element of the Galois group).** Assume the theorem of Fontaine, and let $\ell \ne 2$, $\eta < H$ and $8 H + 1 < \ell$. Let $y \in Y_\eta$ with $\mathrm{Mon}(y) = 0$, and $c \ge 0$ with $\ell^c \zeta(y) \in \mathcal{M}$. Let $b$ be a potential of $y$. Let $g = h k$ with $h \in G_{K_\varpi}$ and $k \in G_{K_\infty}$. Then there is $x \in T$ with
$$\ell^c (g b - b) = 1 \otimes x.$$

Lean: `GlobalTheory.BKGal.MonZero.step_mul`.

*Proof.* We have
$$g b - b = h(k b - b) + (h b - b).$$
By the theorem on the Kummer tower, $k b - b = 1 \otimes x_k$ with $x_k \in T$, so $h(k b - b) = 1 \otimes h x_k$. By [the theorem on coboundaries of potentials](/entry/coboundary-mem-lattice-of-mon-eq-zero/), which uses $\mathrm{Mon}(y) = 0$ and the theorem of Fontaine, $\ell^n (h b - b) \in 1 \otimes T$ for some $n$. By the theorem on lowering the exponent, $\ell^c (h b - b) = 1 \otimes x_h$ with $x_h \in T$. So $\ell^c(g b - b) = 1 \otimes (\ell^c h x_k + x_h)$. $\square$

The point of the lemma is the uniform exponent: $n$ may depend on $h$, but $c$ does not depend on $g$.

**Theorem 7.24.10 (A cocycle with bounded denominators).** Under the hypotheses of the lemma, assume that every element of $G_{\mathbb{Q}_\ell}$ is a product $h k$ with $h \in G_{K_\varpi}$ and $k \in G_{K_\infty}$. Then there is a function $\kappa : G_{\mathbb{Q}_\ell} \to V$ that is the coboundary of $b$ and satisfies $\ell^c \kappa(g) \in T$ for all $g$.

Lean: `GlobalTheory.BKGal.MonZero.exists_cob`.

*Proof.* For each $g$, write $g = h k$ and choose, by [the lemma](/entry/step-mul/), $x(g) \in T$ with $\ell^c (g b - b) = 1 \otimes x(g)$. Put $\kappa(g) = \ell^{-c} x(g)$. Then $\ell^c \kappa(g) = x(g) \in T$. Let $n \ge 0$ and $x \in T$ with $x = \ell^n \kappa(g)$. Then $\ell^c x = \ell^n x(g)$, so
$$\ell^c (1 \otimes x) = \ell^n (1 \otimes x(g)) = \ell^c \cdot \ell^n (g b - b).$$
Since $\mathbb{Q}_\ell \subseteq B_{\mathrm{cris}}$, the element $\ell$ is a unit of $B_{\mathcal{O}}$, and we may cancel $\ell^c$. So $1 \otimes x = \ell^n(g b - b)$, and $\kappa$ is the coboundary of $b$. $\square$

**Theorem 7.24.11 (Galois classes of vectors with zero monodromy).** Assume the theorem of Fontaine. Let $\ell$ be a prime, $\varpi$ a system of roots, and $L$ a finite extension of $\mathbb{Q}_\ell$ that contains the unramified extension of degree $a$, with tame descent data. Fix standard period data for $\mathbb{Q}_\ell$. Let $D$ be a Breuil-Kisin datum of heights $(\eta, H)$ over $\mathcal{O}$, $T$ an $\mathcal{O}$-lattice of $G_{\mathbb{Q}_\ell}$, and $(j, j_B)$ a Galois datum for $(D, T)$ with the standard embeddings. Assume $\eta < H$ and $8 H + 1 < \ell$. Let $y \in Y_\eta$ with $\mathrm{Mon}(y) = 0$, and let $c \ge 0$ with $\ell^c \zeta(y) \in \mathcal{M}$. Then there is $\kappa_1 \in Z^1_f(T)$ that is a Galois class of $\ell^c y$.

Lean: `GlobalTheory.BKGal.classOf_of_mon_eq_zero` (also `GlobalTheory.T.galoisClass_of_monodromy_eq_zero`, a second name).

*Proof.* Since $\eta < H$, we have $H \ge 1$, so $\ell > 9$ and $\ell \ne 2$. By part 1 of the theorem on potentials and classes, $y$ has a potential $b$. By the theorem on decomposition, every $g$ is a product $h k$ as required. By [the previous theorem](/entry/exists-cob/), there is $\kappa$, the coboundary of $b$, with $\ell^c \kappa(g) \in T$ for all $g$. So $\kappa$ is a Galois class of $y$. By the theorem on continuity, $\kappa$ is a continuous cocycle, and by the comparison of period rings it is crystalline. Put $\kappa_1 = \ell^c \kappa$. It is a continuous crystalline cocycle with values in $T$, so $\kappa_1 \in Z^1_f(T)$. By part 3 of the theorem on potentials and classes, $\kappa_1$ is a Galois class of $\ell^c y$. $\square$

The classical analogue is the construction of the crystalline class attached to an extension of filtered $\varphi$-modules, through the exact sequence $0 \to \mathbb{Q}_\ell \to B_{\mathrm{cris}}^{\varphi = 1} \to B_{\mathrm{dR}}/\mathrm{Fil}^0 \to 0$; see Bloch and Kato, §3. Here the extension is replaced by the vector $y$, and the integrality of the class is controlled by $c$.

**Remark 7.24.12 (Formalization).** The inputs are `exists_frobeniusPotential_cocycle_class`, `cocycle_mem_lattice_on_kummerTowerGalois`, `potentialCocycle_mem_lPow_lattice`, `galois_eq_mul_kisinInf_tameSemidirect`, `coboundary_mem_cocycles_odd_prime` and `exists_bcrisTensorLattice_equiv_periodRing`, with [the theorem on coboundaries of potentials](/entry/coboundary-mem-lattice-of-mon-eq-zero/). We read their statements, not their proofs. Of the decomposition theorem only the first of seven parts is used, and of the comparison theorem only the last of four parts ([GaloisClassOfMonodromyEqZero.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/GaloisClassOfMonodromyEqZero.lean#L119)). The lemma and the first theorem are stated for a general coefficient ring $\mathcal{O}$ and embedding $t$; the main theorem specializes them to the ring of integers of $L$ and the standard embedding. The hypothesis $\ell \ne 2$ is not stated in the main theorem: the proof gets it from $\eta < H$ and $8 H + 1 < \ell$ by `omega` (line 104). The definition of a coboundary is `IsCobOf`, and the cancellation step is the helper `cob_of`. The second name is a wrapper that sets `maxHeartbeats` to 1000000.
