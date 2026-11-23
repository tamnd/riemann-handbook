---
title: Reduction modulo p
decls:
  - GlobalTheory.vanishing_charZero_fibre_of_finiteType
  - GlobalTheory.T.kawamata_viehweg_spreading
  - GlobalTheory.Div.vanishing_ample_snc_charZero
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Reduction modulo p

This section proves Kawamata-Viehweg vanishing for a smooth projective variety over a field of characteristic $0$ with a divisor with simple normal crossings ([Theorem 9.4.2](/entry/vanishing-ample-snc-char-zero/)). The proof is the second half of the method of Deligne and Illusie. The variety and its divisor are defined over a ring $R$ of finite type over $\mathbb{Z}$. For a suitable prime $p > \dim X$, $R$ has a map to $\mathbb{Z}/p^2$, and the base change is a lift to $\mathbb{Z}/p^2$ of a variety over $\mathbb{F}_p$, to which Section 3 applies. Semicontinuity then carries the vanishing back to characteristic $0$. Section 5 uses the result to prove vanishing for an effective snc boundary.

For a ring $R$ and a scheme $f : X \to \operatorname{Spec} R$, smooth of relative dimension $d$, a *canonical bundle* of $X$ over $R$ is a line bundle with free generators of $\Omega^d_{X/R}$ on a trivializing affine cover, compatible with the transition functions, as in Section 3. We use relative snc families over $R$ from Section 2.

**Theorem 9.4.1 (Vanishing on a fibre of characteristic $0$).** Let $R$ be a ring of finite type over $\mathbb{Z}$, $k$ a field of characteristic $0$ and $\varphi : R \to k$ an injective ring map. Let $f : X \to \operatorname{Spec} R$ be smooth of relative dimension $d$ and proper, and let $X' = X \times_R k$, with projection $\pi : X' \to X$. Let $(L_i, \sigma_i)_{i \le s}$ be a relative snc family of dimension $d$ on $X$ over $R$, $K$ a canonical bundle of $X$ over $R$, and $M$, $A$ line bundles on $X$ such that $\pi^* A$ is ample. Let $r > 0$ and $0 \leq b_i < r$ be integers with
$$r[M] = r[K] + \sum_i b_i [L_i] + [A] \quad \text{in } \operatorname{Pic} X.$$
Then $H^q(X', \pi^* M) = 0$ for all $q > 0$.

Lean: `GlobalTheory.vanishing_charZero_fibre_of_finiteType` (also `GlobalTheory.T.kawamata_viehweg_spreading`, a second name).

*Proof.* Since $\varphi$ is injective, $R$ is a domain of characteristic $0$. It is noetherian, as it is of finite type over $\mathbb{Z}$. Let $F$ be its field of fractions, so that $\varphi$ factors through $F \subseteq k$.

Step 1 (ampleness on an open set of $\operatorname{Spec} R$). The bundle $A$ is ample on $X'$, so it is ample on the generic fibre $X_F$, since ampleness descends along the field extension $k / F$ for proper schemes. A spreading lemma gives $a \neq 0$ in $R$ with this property: for each field $\kappa$ and each ring map $\chi : R \to \kappa$ with $\chi(a) \neq 0$, the pullback of $A$ to $X \times_R \kappa$ is ample. This is the openness of the ample locus for a proper morphism (EGA III, Theorem 4.7.1).

Step 2 (a point modulo $p^2$). A lemma on rings of finite type over $\mathbb{Z}$ gives a prime $p > d$ and a ring map $\chi : R \to \mathbb{Z}/p^2$ such that $\chi(a)$ is a unit. Let $c : \mathbb{Z}/p^2 \to \mathbb{F}_p$ be the reduction.

Step 3 (the lift). Put $Y = X \times_R \mathbb{Z}/p^2$ and $X_1 = Y \times_{\mathbb{Z}/p^2} \mathbb{F}_p = X \times_R \mathbb{F}_p$, with $\rho : X_1 \to X$. Smoothness of relative dimension $d$ and properness are stable under base change, so $X_1$ is smooth of relative dimension $d$ and proper over $\mathbb{F}_p$. By Step 1 applied to $c \circ \chi$, $\rho^* A$ is ample, so $X_1$ is projective over $\mathbb{F}_p$. The family $(L_i, \sigma_i)$ pulls back to a relative snc family on $Y$ over $\mathbb{Z}/p^2$, the canonical bundle pulls back to a canonical bundle of $X_1$, and the relation pulls back to $X_1$. So [Theorem 9.3.3](/entry/charp-vanishing-liftable/) gives $H^q(X_1, \rho^* M) = 0$ for $q > 0$.

Step 4 (semicontinuity). The kernel of $\varphi$ is $0$, so it is contained in the kernel of $c \circ \chi$: the point of $\operatorname{Spec} R$ under $X'$ is a generization of the point under $X_1$. For a line bundle on a scheme flat and proper over a noetherian base, the vanishing of $H^q$ on the fibre at a point implies the vanishing on the fibre at each generization, by upper semicontinuity of $\dim H^q$ (R. Hartshorne, *Algebraic Geometry*, Theorem III.12.8) and flat base change. Here $f$ is flat since it is smooth. So $H^q(X', \pi^* M) = 0$. $\square$

**Theorem 9.4.2 (Kawamata-Viehweg vanishing with an snc boundary).** Let $k$ be a field of characteristic $0$ and $X$ smooth of relative dimension $d$ and projective over $k$. Let $(L_i, \sigma_i)_{i \le s}$ be a relative snc family of dimension $d$ on $X$ over $k$, $K$ a canonical bundle of $X$, $M$ a line bundle and $A$ an ample line bundle. Let $r > 0$ and $0 \leq b_i < r$ be integers with
$$r[M] = r[K] + \sum_i b_i [L_i] + [A] \quad \text{in } \operatorname{Pic} X.$$
Then $H^q(X, M) = 0$ for all $q > 0$.

Lean: `GlobalTheory.Div.vanishing_ample_snc_charZero`.

Over $\mathbb{C}$ this is the $\mathbb{Q}$-divisor form of [Kawamata-Viehweg vanishing](/learn/positivity-resolution/#kodaira-and-kawamata-viehweg-vanishing) for $M - K \equiv \sum_i \frac{b_i}{r} D_i + \frac1r A$, with $D_i$ the zero divisor of $\sigma_i$, in the special case where the nef and big part is ample (Kawamata, Math. Ann. 261, 1982; Viehweg, J. reine angew. Math. 335, 1982).

*Proof.* $X$ is proper over $k$, since it is projective. A spreading out lemma gives a subring $R \subseteq k$ of finite type over $\mathbb{Z}$, a proper scheme $X_1 \to \operatorname{Spec} R$ with $X = X_1 \times_R k$ and projection $\pi : X \to X_1$, a relative snc family $(L'_i, \sigma'_i)$ of dimension $d$ on $X_1$ over $R$ and a line bundle $M_1$ on $X_1$, with $\pi^*[L'_i] = [L_i]$ and $\pi^*[M_1] = [M]$. The snc charts make $X_1$ smooth of relative dimension $d$ over $R$. A canonical bundle $K_1$ of $X_1$ over $R$ exists, and $\pi^*[K_1] = [K]$. Let $A_1$ be a line bundle with class $r[M_1] - r[K_1] - \sum_i b_i [L'_i]$. Then $\pi^*[A_1] = r[M] - r[K] - \sum_i b_i [L_i] = [A]$, so $\pi^* A_1$ is ample. Now the last theorem, with $\varphi$ the inclusion $R \subseteq k$, gives $H^q(X, \pi^* M_1) = 0$ for $q > 0$. Since $\pi^* M_1 \cong M$, the theorem follows. $\square$

**Remark 9.4.3 (Formalization).** The four lemmas of the first proof are `AmpleSpread.relAmple_spread` (Step 1), `FibreAmple.relAmple_of_fieldExtension` (ampleness under field extension), `exists_ringHom_zmod_prime_sq_isUnit_of_finiteType` (Step 2) and `SemicontLB.subsingleton_coh_pull_of_ker_le` (Step 4); the second proof uses `GlobalTheory.T.spread_out_relative_snc` and `GlobalTheory.T.smoothOfRelativeDimension_of_relSncDivisor`. We read their statements and cite the classical results that they express; we did not check that their proofs follow those sources. In [KawamataViehwegVanishing.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/KawamataViehwegVanishing.lean#L20) the smoothness of $X$ is a hypothesis, but it also follows from the relative snc family, as it does for $X_1$ in the proof; projectivity is used only to get properness. A canonical bundle $K_1$ of $X_1$ comes from `CanonLB.nonempty`, and $A_1$ from the surjectivity of the class map `cls_surj`. The second name `GlobalTheory.T.kawamata_viehweg_spreading` is proved by `first | exact @… | …`.
