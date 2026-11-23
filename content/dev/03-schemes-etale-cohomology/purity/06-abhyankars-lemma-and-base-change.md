---
title: Abhyankar's lemma and base change
decls:
  - GlobalTheory.KeyOriginEnlarge.etale_enlarge
  - GlobalTheory.T.baseChange_integralClosure_etale_height_one
  - GlobalTheory.KeyOriginBC.etale_bc
  - GlobalTheory.T.integralClosure_torsor_etale_height_one_abhyankar
  - GlobalTheory.KeyOriginBC.closureEtaleAt_of_mem_height_le_one
  - GlobalTheory.T.generic_fibre_base_change_injective
  - GlobalTheory.AbhHeightOne.closureEtaleAt_of_root_of_uniformiser
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Abhyankar's lemma and base change

This section and the next two prove [the theorem on étale enlargement by roots of uniformisers](/entry/etale-enlarge-by-uniformiser-roots/), the last step of the enlargement to a good model. We keep the notation of the section on cyclic torsors. So $T$ is an absolutely integrally closed local domain, $O$ is a strict henselisation of $T[x]$ at the origin $\mathfrak{m}[x] + (x)$, and $q \geq 1$ is a unit in $T$. We fix fitting data $(A, i, E_A, Q_A, j, \psi, D_A)$. So $A$ is a [[noetherian|0670T59HGE]], normal, local domain, essentially of finite type over $\mathbb{Z}$, with an injective local map $i : A \to T$, and $q$ is a unit in $A$. The ring $R = (E_A)_{Q_A}$ is the local ring of an étale $A[x]$-algebra at a prime over the origin, with maps $j : R \to O$ and $\psi$ on generic fibres. Finally $D_A$ is a $\mathbb{Z}/q$-torsor over the generic fibre $R_K$ of $R$, and $C$ is the closure of $R$ in $D_A$.

The plan is classical. The torsor $D_A$ is étale over the generic fibre, so its closure $C$ is étale over $R$ away from the zeros of one nonzero element $a \in A$. Over the finitely many height one primes of $A$ that contain $a$, the torsor can ramify. The ramification is tame, because $q$ is a unit. By Abhyankar's lemma, the ramification goes away after we adjoin $q$-th roots of local uniformisers of these primes. This makes the closure étale at every prime of height at most $1$. The purity theorem of Zariski and Nagata then extends étaleness to all primes $\mathfrak{P}$ of $R$ with $\operatorname{ht}(\mathfrak{P} \cap A) \leq 1$, which is condition 1 of goodness.

**Definition 2.6.1 (Étale at a prime).** Let $A$ be a domain, $R$ an $A$-algebra, $D$ an algebra over the generic fibre $R_K$, and $C$ the closure of $R$ in $D$. For a prime $\mathfrak{P}$ of $R$, we say that $C$ is *étale at* $\mathfrak{P}$ if $R_{\mathfrak{P}} \otimes_R C$ is [[étale|FTRW0679E2]] over $R_{\mathfrak{P}}$.

With this word, condition 1 of goodness says that $C$ is étale at every prime $\mathfrak{P}$ of $R$ with $\operatorname{ht}(\mathfrak{P} \cap A) \leq 1$.

### The proof of étale enlargement

**Theorem 2.6.2 (Étale enlargement, the proof).** [The theorem on étale enlargement by roots of uniformisers](/entry/etale-enlarge-by-uniformiser-roots/) holds.

Lean: `GlobalTheory.KeyOriginEnlarge.etale_enlarge`.

*Proof.* We have the data above, a retraction $\rho : R \to A$ with kernel $(x)$ that agrees with $j$ modulo $x$, and a point at zero $s : C \to \operatorname{Frac}(A)$ over $\rho$.

Step 1. We take as given that there is $a \neq 0$ in $A$ such that $C$ is étale at every prime $\mathfrak{P}$ of $R$ with $a \notin \mathfrak{P}$.

Step 2. We take as given that there are a noetherian, normal, local domain $A_1$, essentially of finite type over $\mathbb{Z}$, with an injective map $f : A \to A_1$ and an injective local map $i_1 : A_1 \to T$ with $i_1 \circ f = i$, such that the following holds. For every height one prime $\mathfrak{p}_1$ of $A_1$ with $f(a) \in \mathfrak{p}_1$, the prime $\mathfrak{p} = f^{-1}(\mathfrak{p}_1)$ has height one, and there are $\pi \in A$ that is a uniformiser of the [[discrete valuation ring|MGM3CNJW9V]] $A_{\mathfrak{p}}$ and $y \in A_1$ with $y^q = f(\pi)$. In words, $A_1$ contains $q$-th roots of local uniformisers at the height one primes over $a$; such roots exist in $T$, because $T$ is absolutely integrally closed.

Step 3. [The base change theorem](/entry/base-change-integral-closure-etale-height-one/) below gives data $E_{A_1}$, $Q_{A_1}$, $j_1$, $\psi_1$, $D_{A_1}$ over $A_1$ of the same kind, a retraction $\rho_1$ with a point at zero, and maps $\beta$, $h$ compatible with $\psi$. It also says that the closure $C_1$ of $R_1 = (E_{A_1})_{Q_{A_1}}$ in $D_{A_1}$ is étale at every prime of $R_1$ of height at most $1$.

Step 4. [The purity theorem for the closure](/entry/integral-closure-etale-at-of-height-le-one-purity/) of the next section makes $C_1$ étale at every prime $\mathfrak{P}_1$ of $R_1$ with $\operatorname{ht}(\mathfrak{P}_1 \cap A_1) \leq 1$. This is condition 1 of goodness for the new data. Condition 2 is the point at zero of step 3. $\square$

Lean: `GlobalTheory.T.exists_ne_zero_closureEtaleAt_alt` (also `GlobalTheory.T.exists_kummerEnlargement_rootsOfUniformisers`).

**Remark 2.6.3.** Steps 3 and 4 make the closure étale in two stages: base change gives étaleness only at primes of height at most $1$ in $R_1$ itself, and purity passes to the larger set of primes whose contraction to $A_1$ has height at most $1$.

### Base change to the Kummer enlargement

**Theorem 2.6.4 (Base change to a Kummer enlargement).** Let $T$, $O$, $q$, $A$, $R$, $D_A$, $\rho$ and $s$ be as in the étale enlargement theorem. Let $a \neq 0$ in $A$ be such that $C$ is étale at every prime of $R$ that does not contain $a$. Let $A_1$ be a noetherian, normal, local domain, essentially of finite type over $\mathbb{Z}$, and let $f : A \to A_1$ and $i_1 : A_1 \to T$ be ring maps such that $f$ is injective, $i_1$ is injective and local, and $i_1 \circ f = i$. Assume that for every height one prime $\mathfrak{p}_1$ of $A_1$ with $f(a) \in \mathfrak{p}_1$, the prime $f^{-1}(\mathfrak{p}_1)$ has height one, and there are $\pi \in A$ that is a uniformiser of $A_{f^{-1}(\mathfrak{p}_1)}$ and $y \in A_1$ with $y^q = f(\pi)$. Then there are an étale $A_1[x]$-algebra $E_{A_1}$, a prime $Q_{A_1}$ over the origin, maps $j_1$ and $\psi_1$ to $O$ and $O_K$, and a $\mathbb{Z}/q$-torsor $D_{A_1}$ over the generic fibre of $R_1 = (E_{A_1})_{Q_{A_1}}$, such that $(A_1, i_1, E_{A_1}, Q_{A_1}, j_1, \psi_1, D_{A_1})$ are fitting data and:

1. there is a retraction $\rho_1 : R_1 \to A_1$ with kernel $(x)$ that agrees with $j_1$ modulo $x$, with a point at zero;
2. the closure $C_1$ of $R_1$ in $D_{A_1}$ is étale at every prime of $R_1$ of height at most $1$;
3. there are maps $\beta$ of generic fibres and $h : D_A \to D_{A_1}$ with $\psi_1 \circ \beta = \psi$ and $h$ over $\beta$.

Lean: `GlobalTheory.T.baseChange_integralClosure_etale_height_one` (also `GlobalTheory.KeyOriginBC.etale_bc`).

*Proof.* Let $E_1 = A_1[x] \otimes_{A[x]} E_A$. It is étale over $A_1[x]$, as a base change of an étale algebra. The maps $A_1[x] \to T[x] \to O$ and $E_A \to R \to O$ agree on $A[x]$, so they give a map $E_1 \to O$. Let $Q_1$ be the inverse image of the maximal ideal of $O$. We take as given that $Q_1$ lies over the origin of $A_1[x]$. Put $R_1 = (E_1)_{Q_1}$, and let $j_1 : R_1 \to O$ be the induced local map. Let $\beta : R_K \to (R_1)_{K_1}$ be the map of generic fibres, and let $D_{A_1} = (R_1)_{K_1} \otimes_{R_K} D_A$, with the action of $\mathbb{Z}/q$ on the second factor. A base change of a $\mathbb{Z}/q$-torsor is a $\mathbb{Z}/q$-torsor, and $h$ is $d \mapsto 1 \otimes d$.

The retraction $\rho_1$ is the reduction $x \mapsto 0$. We take as given that its kernel is $(x)$, and that the point at zero $s$ moves along the base change to a point at zero for $\rho_1$. It remains to show that $C_1$ is étale at a prime $\mathfrak{P}_1$ of $R_1$ of height at most $1$. There are two cases.

If $f(a) \notin \mathfrak{P}_1$, then the inverse image $\mathfrak{P}$ of $\mathfrak{P}_1$ in $R$ does not contain $a$, so $C$ is étale at $\mathfrak{P}$. We take as given that this property survives the base change, so $C_1$ is étale at $\mathfrak{P}_1$. If $f(a) \in \mathfrak{P}_1$, apply [the theorem on primes that contain $a$](/entry/integral-closure-torsor-etale-height-one-abhyankar/) below. $\square$

Lean: `GlobalTheory.T.comap_maximalIdeal_eq_origin` (also `GlobalTheory.T.ker_baseChangedReduction_eq_span_X`, `GlobalTheory.T.localization_at_prime_etale_compat` and `GlobalTheory.T.normal_local_ring_etale_base_change`).

### Primes that contain a

**Theorem 2.6.5 (Primes that contain $a$).** Let $T$ be a ring and $O$ a local $T[x]$-algebra. Let $A$ and $A_1$ be noetherian, normal, local domains, essentially of finite type over $\mathbb{Z}$, and let $f : A \to A_1$, $i : A \to T$ and $i_1 : A_1 \to T$ be ring maps with $f$ injective and $i_1 \circ f = i$. Let $E_A$ be an étale $A[x]$-algebra, $Q_A$ a prime of $E_A$, $R = (E_A)_{Q_A}$, and $j : R \to O$ a ring map whose restriction to $A[x]$ is $A[x] \to T[x] \to O$. Let $q \geq 1$ be a unit in $A$, let $D_A$ be a $\mathbb{Z}/q$-torsor over $R_K$, and let $a \neq 0$ in $A$ satisfy the condition on height one primes of the base change theorem. Let $R_1$ be the localization of $A_1[x] \otimes_{A[x]} E_A$ at the inverse image of the maximal ideal of $O$, and $C_1$ the closure of $R_1$ in $(R_1)_{K_1} \otimes_{R_K} D_A$. Then $C_1$ is étale at every prime $\mathfrak{P}_1$ of $R_1$ of height at most $1$ with $f(a) \in \mathfrak{P}_1$.

Lean: `GlobalTheory.T.integralClosure_torsor_etale_height_one_abhyankar` (also `GlobalTheory.KeyOriginBC.closureEtaleAt_of_mem_height_le_one`).

*Proof.* The rings $R$ and $R_1$ are domains, and $A \to R$ and $A_1 \to R_1$ are injective, because both are localizations of étale algebras over polynomial rings over normal domains. Since $a \neq 0$ and $f$ is injective, $\mathfrak{P}_1 \neq 0$, so $\mathfrak{P}_1$ has height $1$. The map $A_1[x] \to R_1$ is a localization of an étale map, so the prime $\mathfrak{P}_1 \cap A_1[x]$ has [[height|87WH65FJB8]] $1$. It contains the extension $\mathfrak{p}_1 A_1[x]$ of $\mathfrak{p}_1 = \mathfrak{P}_1 \cap A_1$, which is a nonzero prime because it contains $f(a)$. Hence $\mathfrak{P}_1 \cap A_1[x] = \mathfrak{p}_1 A_1[x]$, and $\mathfrak{p}_1$ has height $1$.

By the condition on height one primes, the prime $\mathfrak{p} = f^{-1}(\mathfrak{p}_1)$ of $A$ has height $1$, and there are a uniformiser $\pi$ of $A_{\mathfrak{p}}$ and $y \in A_1$ with $y^q = f(\pi)$. The ring $A_1[x]$ localized at $\mathfrak{p}_1 A_1[x]$ is a discrete valuation ring, since $A_1$ is normal and $\mathfrak{p}_1$ has height $1$. A local ring that is a localization of an étale algebra over a discrete valuation ring, at a prime over the maximal ideal, is again a discrete valuation ring with the same uniformiser. So $(R_1)_{\mathfrak{P}_1}$ is a discrete valuation ring. The same argument applies to the inverse image $\mathfrak{P}$ of $\mathfrak{P}_1$ in $R$, which lies over $\mathfrak{p}$: the ring $R_{\mathfrak{P}}$ is a discrete valuation ring, and $\pi$ is a uniformiser of it. Now [Abhyankar's lemma for cyclic torsors](/entry/generic-fibre-base-change-injective/) applies, with the image of $y$ in $R_1$. $\square$

Lean: `GlobalTheory.T.height_one_contraction_of_etale_prime` (also `GlobalTheory.T.height_one_prime_over_constant_ideal`).

In this proof we take as given the facts on heights of primes under localizations of étale maps, and that a localization of an étale algebra over a discrete valuation ring at a prime over the maximal ideal is a discrete valuation ring with the same uniformiser.

### Abhyankar's lemma

The classical statement is about a finite separable extension of the fraction field of a discrete valuation ring.

**Theorem 2.6.6 (Abhyankar's lemma).** Let $S$ be a discrete valuation ring with fraction field $K$ and uniformiser $\pi$, and let $L$ be a finite separable extension of $K$ that is tamely ramified over $S$, with ramification indices that divide an integer $n$ that is a unit in $S$. Let $S \to S_1$ be a local map to a discrete valuation ring with fraction field $K_1$, such that $\pi = y^n$ for some $y \in S_1$. Then the integral closure of $S_1$ in $K_1 \otimes_K L$ is étale over $S_1$.

This is a special case of SGA 1, Exposé XIII, Lemme 5.2. We use a form for cyclic torsors over the generic fibre of a pair of domains.

**Theorem 2.6.7 (Abhyankar's lemma for cyclic torsors).** Let $A \subset R$ and $A_1 \subset R_1$ be domains, with fraction fields $K$ and $K_1$ of $A$ and $A_1$, and let $f : A \to A_1$ and $\varphi : R \to R_1$ be compatible ring maps with $f$ injective. Let $\beta : R_K \to (R_1)_{K_1}$ be a map of generic fibres compatible with $\varphi$. Let $q \geq 1$ be a unit in $A$, and let $D_A$ be a $\mathbb{Z}/q$-torsor over $R_K$. Let $\mathfrak{P}_1$ be a prime of $R_1$ such that $(R_1)_{\mathfrak{P}_1}$ and $R_{\mathfrak{P}}$ are discrete valuation rings, where $\mathfrak{P} = \varphi^{-1}(\mathfrak{P}_1)$. Assume that some $\pi \in A$ is a uniformiser of $R_{\mathfrak{P}}$, and that $y^q = \varphi(\pi)$ for some $y \in R_1$. Then the closure of $R_1$ in $(R_1)_{K_1} \otimes_{R_K} D_A$ is étale at $\mathfrak{P}_1$.

Lean: `GlobalTheory.T.generic_fibre_base_change_injective` (also `GlobalTheory.AbhHeightOne.closureEtaleAt_of_root_of_uniformiser`).

*Proof.* Put $S = R_{\mathfrak{P}}$ and $S_1 = (R_1)_{\mathfrak{P}_1}$. The integral closure commutes with [[localization|X6JD4AG973]], so it is enough to show that the integral closure of $S_1$ in the localization of $(R_1)_{K_1} \otimes_{R_K} D_A$ is étale over $S_1$. The element $\pi$ is a nonzero element of $A$, so it is inverted in $R_K$. Hence the localization of $R_K$ at $\mathfrak{P}$ is the fraction field $F$ of $S$, and the localization of $(R_1)_{K_1}$ at $\mathfrak{P}_1$ is the fraction field $F_1$ of $S_1$. So we must show that the integral closure of $S_1$ in $F_1 \otimes_F (F \otimes_{R_K} D_A)$ is étale over $S_1$.

The algebra $F \otimes_{R_K} D_A$ is a $\mathbb{Z}/q$-torsor over the field $F$. A $\mathbb{Z}/q$-torsor over a field is a finite product of Galois extensions $L_1, \dots, L_r$ of $F$, each with a degree that divides $q$. Since $q$ is a unit in $S$, each $L_k$ is tamely ramified over $S$, with [[ramification indices|H5RC67SD24]] that divide $q$ and separable residue field extensions. By Abhyankar's lemma, with $n = q$ and $y$, the integral closure of $S_1$ in $F_1 \otimes_F L_k$ is étale over $S_1$ for each $k$. The integral closure of $S_1$ in a finite product is the product of the integral closures, and a finite product of étale algebras is étale. $\square$

Lean: `GlobalTheory.AbhHeightOne.closureEtaleAt_of_etale_integralClosure_localization` (also `GlobalTheory.T.zmodTorsor_field_eq_prod_galois`, `GlobalTheory.T.ramificationIdx_dvd_of_galois_degree_dvd_unit_dvr` and `GlobalTheory.T.abhyankar_etale_integralClosure_root_uniformizer`).

In this proof we take as given the structure of $\mathbb{Z}/q$-torsors over a field, the bound on ramification indices, and Abhyankar's lemma.

**Remark 2.6.8 (Formalization).** The last line of the proof of étale enlargement rewrites goodness with a lemma that holds by definition: [GoodIffEtaleAt.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/GoodIffEtaleAt.lean#L19). For the two steps of that proof, the four facts of the base change proof, the two facts on heights, and the last three facts of the proof of Abhyankar's lemma for cyclic torsors, we read the statements, not the proofs. Some names do not describe their statements. The lemma that moves the point at zero along the base change has a name about étale maps and localization: [LocalizationAtPrimeEtaleCompat.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LocalizationAtPrimeEtaleCompat.lean#L7). The lemma for the case $f(a) \notin \mathfrak{P}_1$ has a name about normal local rings: [NormalLocalRingEtaleBaseChange.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/NormalLocalRingEtaleBaseChange.lean#L7). The name of Abhyankar's lemma for cyclic torsors speaks of the injectivity of a map of generic fibres: [GenericFibreBaseChangeInjective.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/GenericFibreBaseChangeInjective.lean#L7), and the module that holds its proof has a name that does not describe it either. The lemma that passes from fraction fields to the localized closure takes the field case as an argument: [M2ModelEstablished.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/M2ModelEstablished.lean#L65). Several statements ask for $0 < q$ besides $q$ being a unit; the first follows from the second. The theorem on primes that contain $a$ does not ask for $Q_A$ to lie over the origin, nor for $C$ to be étale away from $a$. The statements of this section that have two names import Mathlib twice and raise the heartbeat limit, for example [BaseChangeIntegralClosureEtaleHeightOneStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/BaseChangeIntegralClosureEtaleHeightOneStatement.lean#L10).
