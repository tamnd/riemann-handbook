---
title: Wach rings over a tame subextension
decls:
  - GlobalTheory.T.wachModule_descent_to_tame_subextension
  - GlobalTheory.NL.p9_statement
  - GlobalTheory.DelParam.torsion_parameters
  - GlobalTheory.DelParam.exists_eisenstein
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Wach rings over a tame subextension

Let $K_0$ be a finite unramified extension of $\mathbb{Q}_p$ and let $K$ lie between $K_0$ and $K_0(\mu_p)$. The ring of [Wach modules](/learn/padic-hodge/#lattices-wach-breuil-kisin-and-prismatic-f-crystals) over $K_0(\mu_{p^\infty})$ has the variable $\pi$ with $\varphi(\pi) = (1+\pi)^p - 1$. Over $K$ one wants a variable that is invariant under the group $\Delta = \mathrm{Gal}(K_0(\mu_p)/K)$. This section constructs such a variable $\pi'$, shows that $\varphi$ and $\gamma$ act on it through an Eisenstein polynomial of a uniformizer of $K$, and proves that the Wach module of a crystalline lattice descends to $\pi'$. The result is one of the clauses on Wach lattices in [Theorem 6.5.4](/entry/wach-used-clauses/), which is an input of the step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/).

In the local sections of this chapter the prime is written $p$; it is the prime $\ell$ of the global sections.

### Wach data

Let $K$ be a finite extension of $\mathbb{Q}_p$ in $\overline{\mathbb{Q}}_p$, let $K_0 = K \cap \mathbb{Q}_p^{\mathrm{ur}}$ be its maximal unramified subfield, and let $n = [K_0 : \mathbb{Q}_p]$. For $s \geq 1$ put $K_s = K_0(\mu_{p^s})$. Let $L$ be a finite extension of $\mathbb{Q}_p$ with ring of integers $\mathcal{O}$ and a valuation $v$ with $v(p) = 1$.

**Definition 6.3.1 (Good triple).** The triple $(K, s, L)$ is *good* if $s \geq 1$, $s \geq 2$ when $p = 2$, $K \subseteq K_s$, and every embedding of $K_s$ into $\overline{\mathbb{Q}}_p$ has image in $L$.

Lean: `Formalism.BasicNotions.Loc.Good`.

So $K$ is a subextension of $K_s/K_0$. For $s = 1$ and $p \neq 2$ the extension $K_1/K_0$ is tamely and totally ramified of degree $p - 1$, and $K$ is a tame subextension: $e = [K : K_0]$ divides $p - 1$.

The ring of *letters* is $A = \prod_{i \in \mathbb{Z}/n} \mathcal{O}[[X]]$, one factor for each embedding of $K_0$ into $L$. Write $\pi = (X, \dots, X)$ and $e_i$ for the idempotent of the factor $i$.

**Definition 6.3.2 (Wach datum).** A *Wach datum* for a good triple $(K, s, L)$ consists of the following objects.

1. A bijection $i \mapsto \tau_i$ from $\mathbb{Z}/n$ to the embeddings $K_0 \to L$, with $\tau_{i+1} \circ \sigma = \tau_i$ for the Frobenius $\sigma$ of $K_0$.
2. An $\mathcal{O}$-algebra endomorphism $\varphi_0$ of $\mathcal{O}[[X]]$ with $\varphi_0(X) = X q_0$, where $X q_0 = (1+X)^p - 1$. On $A$, $\varphi$ sends the letter $i - 1$ to the letter $i$ through $\varphi_0$.
3. A commutative group $\Gamma$ with a surjection $G_{\mathbb{Q}_p} \to \Gamma$, an injective character $\chi : \Gamma \to \mathcal{O}^\times$ that lifts the cyclotomic character, and an action $g \mapsto \gamma_g$ of $\Gamma$ on $\mathcal{O}[[X]]$ that commutes with $\varphi_0$ and has $\gamma_g(X) = \chi(g) X + O(X^2)$. It acts on $A$ letter by letter.
4. An element $\gamma \in \Gamma$ with $v(\chi(\gamma) - 1) = s$, and the torsion subgroup $\Delta \subseteq \Gamma$.
5. A $p$-adically complete ring $\mathcal{E} \supseteq A$ in which $\pi$ is a unit and $A$ is dense, with extensions of $\varphi$ and of the action of $\Gamma$.
6. For each lattice $T$ in a $p$-adic representation of $G_{\mathbb{Q}_p}$: a free $\mathcal{E}$-module $D(T)$ of rank $\mathrm{rank}_{\mathcal{O}} T$ with commuting semilinear $\varphi$ and $\Gamma$, and an $A$-submodule $N(T) \subseteq D(T)$, the *Wach module*.

The Wach module satisfies: $N(T)$ is finitely generated and stable under $\Gamma$; $(\gamma_g - 1)N(T) \subseteq \pi N(T)$; if $T$ is crystalline then $\mathcal{E} \otimes_A N(T) = D(T)$; and $\varphi$ preserves $N(T)$, and $N(T)$ lies in the span of $\varphi(N(T))$, up to powers of $Q = \varphi^{s-1}(q)$, where $q = (q_0, \dots, q_0)$. The datum also gives a map $\mathrm{cl}$ from Herr cocycles to $H^1(G_{K_s}, T)$ and a comparison map from $N(T)$ to $D_{\mathrm{cris}}(T)$, used in the next sections.

Lean: `Formalism.BasicNotions.Loc.LocWach`.

Put $X_s = \varphi^{s-1}(\pi)$, and let $A^\Delta$ be the subring of elements fixed by $\Delta$ and $N^\Delta(T)$ the part of $N(T)$ fixed by $\Delta$. In the classical case $\Gamma = \mathrm{Gal}(K_0(\mu_{p^\infty})/K_0) \cong \mathbb{Z}_p^\times$, $\Delta \cong \mu_{p-1}$ for $p \neq 2$, and $N(T)$ is the module of Wach and Berger.

### Eisenstein data

**Definition 6.3.3 (Eisenstein datum).** Let $\xi \in \mathcal{O}[[X]]$ and $e \geq 1$. A monic polynomial $E \in \mathcal{O}[Y]$ is an *Eisenstein polynomial for $\xi$ of degree $e$* if

1. $\deg E = e$, $p$ divides each coefficient of $E$ below degree $e$, and $E(0)$ is $p$ times a unit;
2. $E(\xi)$ is a unit multiple of $q_0$;
3. $\varphi_0(\xi) = c(\xi) \, \xi \, E(\xi)^{|\Delta|}$ for a unit $c \in \mathcal{O}[[X]]$;
4. $\gamma(\xi) - \xi = c'(\xi) \, \xi \, E(\xi)$ for a unit $c' \in \mathcal{O}[[X]]$.

We say that $\xi$ *has Eisenstein roots of degree $e$* if some Eisenstein polynomial $E$ for $\xi$ of degree $e$ has the form $E = \prod_{\tau = 1}^{e} (Y - \varpi_\tau)$ with distinct $\varpi_\tau \in \mathcal{O}$, each $\varpi_\tau^e$ is a unit multiple of $p$, and for each $\tau$ there is a primitive $p$-th root of unity $\zeta$ with $X - (\zeta - 1)$ dividing $\xi - \varpi_\tau$.

Lean: `GlobalTheory.DelParam.EisAt` (also `GlobalTheory.DelParam.HasEis`, the second notion).

Condition 1 says that $E$ is an Eisenstein polynomial in the usual sense. The last condition says that $\varpi_\tau$ is the value of $\xi$ at $X = \zeta - 1$, a uniformizer of $\mathbb{Q}_p(\mu_p)$.

**Lemma 6.3.4 (Eisenstein roots of the invariant variable).** Let $(K, 1, L)$ be good, $p \neq 2$, and fix a Wach datum. Let $\xi \in \mathcal{O}[[X]]$ be fixed by $\Delta$ and a unit multiple of $X^{|\Delta|}$. Then $\xi$ has Eisenstein roots of degree $[K : K_0]$.

Lean: `GlobalTheory.DelParam.exists_eisenstein`.

*Proof.* The invariants of $\Delta$ in $\mathcal{O}[[X]]$ form a ring of power series in one variable. There are a second Wach-type ring $\mathcal{O}[[Y]]$, with Frobenius, $\gamma$ and polynomial $E$, and an injective $\mathcal{O}$-algebra map $j : \mathcal{O}[[Y]] \to \mathcal{O}[[X]]$. Its image is the ring of $\Delta$-invariants, $j$ intertwines the Frobenius and $\gamma$ of the two rings, $j(Y)$ is a unit multiple of $X^{|\Delta|}$, and $j(E)$ is a unit multiple of $q_0$. In this ring the polynomial $E$ is the product of $Y - \varpi_\tau$ over the values $\varpi_\tau$ of $Y$ at the points $\zeta - 1$, and these values are distinct with $\varpi_\tau^e$ associated to $p$. Transporting the relations through $j$ gives conditions 1 to 4 for $j(Y)$. The degree of $E$ is the ramification index of $K/K_0$. Since $j(Y)$ and $\xi$ are both $\Delta$-invariant unit multiples of $X^{|\Delta|}$, one can take $j(Y) = \xi$. $\square$

### The relations of the Wach ring

**Definition 6.3.5 (Wach ring relations).** Let $e, s' \geq 1$, let $\pi' \in A$ and let $E_i \in \mathcal{O}[Y]$ for $i \in \mathbb{Z}/n$. Write $E(\pi')$ for the element with letters $E_i(\pi'_i)$. The pair $(\pi', E)$ *satisfies the Wach ring relations of type $(e, s')$* if:

1. $\pi' \in A^\Delta$, and every $a \in A^\Delta$ is $f(\pi')$ for a unique family $f$ of power series;
2. $\pi' = w \pi^{s'}$, $q = w' E(\pi')$, $\varphi(\pi') = w'' \pi' E(\pi')^{s'}$ and $\gamma(\pi') - \pi' = w''' \pi' E(\pi')$ for units $w, w', w'', w'''$ of $A$;
3. each $E_i$ has degree $e$;
4. there is $E_0 \in K_0[Y]$ with $\tau_i(E_0) = E_i$ for all $i$, and a root $\varpi \in K$ of $E_0$ with $v(\tau \varpi) = 1/e$ for every embedding $\tau : K \to L$.

The Wach module of $T$ is *free over the letters in $\pi'$* if there are $b_1, \dots, b_r \in N^\Delta(T)$ such that each $x \in N(T)$ is $\sum a_j b_j$ for unique $a_j \in A$, each $x \in N^\Delta(T)$ is such a sum with $a_j \in A^\Delta$, and $(\gamma - 1) N^\Delta(T) \subseteq \pi' N^\Delta(T)$.

Lean: `Formalism.MainNotions.DeltaInvariantLattices.wachRingRelations` (also `Formalism.MainNotions.DeltaInvariantLattices.wachModuleOverLetters`, the second notion).

Condition 4 says that $E_0$ is the minimal polynomial of a uniformizer $\varpi$ of $K$ over $K_0$, so $E$ is an Eisenstein polynomial of $K/K_0$. Over $\pi'$ the ring $A^\Delta$ then looks like the Wach ring of $K$: $\varphi(\pi')$ is $\pi'$ times a power of $E(\pi')$, as $\varphi(\pi) = \pi q$ over $K_0(\mu_{p^\infty})$.

**Proposition 6.3.6 (Parameters of the tame subextension).** Let $(K, s, L)$ be good with a Wach datum, $s = 1$ and $p \neq 2$. Put $e = [K : K_0]$. Then:

1. $|\Delta| = (p - 1)/e$;
2. some $(\pi', E)$ satisfies the Wach ring relations of type $(e, (p-1)/e)$;
3. if $K = K_0$, then $\pi_0 = (\varpi_0, \dots, \varpi_0)$ with $\varpi_0 = 1 - p + \sum_{\delta \in \Delta} \delta(1 + X)$, and $E_i = Y + p$, satisfy the Wach ring relations of type $(1, p - 1)$.

Lean: `GlobalTheory.DelParam.torsion_parameters`.

*Proof.* For 1, one shows $|\Delta| \cdot [K : K_0] = p - 1$. Classically $\Delta$ is $\mathrm{Gal}(K_1/K)$, and $K_1/K_0$ is totally ramified of degree $p - 1$. For 2 let $\xi = \prod_{\delta \in \Delta} \delta(X)$. It is $\Delta$-invariant, and it is a unit multiple of $X^{|\Delta|}$ since each $\delta(X)$ is $\chi(\delta) X$ times a unit. By [Lemma 6.3.4](/entry/exists-eisenstein/), $\xi$ has Eisenstein roots $\varpi_\tau$ of degree $e$. Each $\varpi_\tau$ is a product $\prod_{\delta}(\zeta^{a_\delta} - 1)$ over $\Delta$, and an element $g$ of $G_K$ acts on $\zeta$ through an element of $\Delta$, so it permutes the factors and fixes $\varpi_\tau$. Hence $\varpi = \varpi_1 \in K$, and $E$ comes from a polynomial $E_0 \in K_0[Y]$. The valuation of each conjugate of $\varpi$ is $1/e$ because $\varpi^e$ is associated to $p$. Put $\pi' = (\xi, \dots, \xi)$. The invariants of $\Delta$ in $\mathcal{O}[[X]]$ are the power series in $\xi$, and $\mathcal{O}[[X]]$ is free over them with basis $1, X, \dots, X^{|\Delta| - 1}$. With the relations of the Eisenstein datum, this gives the Wach ring relations. For 3, when $K = K_0$, $\Delta$ has order $p - 1$ and $\varpi_0 = 1 - p + \sum_{\delta} \delta(1+X)$ is the trace of $1 + X$ shifted by $1 - p$. It is $\Delta$-invariant and a unit multiple of $X^{p-1}$, and its Eisenstein polynomial of degree 1 is $Y + p$, because $\varpi_0(\zeta - 1) = 1 - p + \sum_{a \in \mathbb{F}_p^\times} \zeta^a = -p$. The same argument then gives the relations of type $(1, p-1)$. $\square$

**Theorem 6.3.7 (Descent of Wach modules to the tame subextension).** Let $(K, s, L)$ be good with a Wach datum, $s = 1$ and $p \neq 2$, and let $T$ be a crystalline lattice. Put $e = [K : K_0]$. Then $|\Delta| = (p - 1)/e$; there is $(\pi', E)$ that satisfies the Wach ring relations of type $(e, (p-1)/e)$ and over which $N(T)$ is free over the letters; and if $K = K_0$, the pair $(\pi_0, Y + p)$ satisfies the relations of type $(1, p-1)$ and $N(T)$ is free over the letters in $\pi_0$.

Lean: `GlobalTheory.NL.p9_statement` (also `GlobalTheory.T.wachModule_descent_to_tame_subextension`, a second name).

*Proof.* The Proposition gives the order of $\Delta$ and the two pairs. Given a pair $(\pi', E)$ that satisfies the Wach ring relations with $s' > 0$, the Wach module $N(T)$ has a basis of $\Delta$-invariant vectors over $A$, and $N^\Delta(T)$ is spanned by them over $A^\Delta$. The reason is that $\Delta$ is a finite group of order prime to $p$ acting semilinearly on the free module $N(T)$, so its invariants form a free module over the invariant ring $A^\Delta$ that generates $N(T)$; and $(\gamma - 1)N(T) \subseteq \pi N(T)$ becomes $(\gamma - 1)N^\Delta(T) \subseteq \pi' N^\Delta(T)$ after taking invariants. We apply this with $s' = |\Delta| > 0$ (as $\Delta$ contains $1$) and with $s' = p - 1 > 0$. $\square$

**Remark 6.3.8 (Formalization).** The Wach datum is the structure `LocWach` in [DataNLoc.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/DataNLoc.lean#L164). Its objects $\mathcal{E}$, $D(T)$, $N(T)$ and all their properties are fields: nothing in this chapter constructs a Wach module, and the theorems hold for every datum. The proof of the Lemma rests on the auxiliary ring and the map $j$ from `exists_attached` and on `eisenstein_gen`; the descent of the basis is `GlobalTheory.T.wachLattice_deltaInvariant_basis`. We did not open the proofs of `exists_attached`, `card_torsion_mul_finrank` or of the basis lemma, so the reasons given for them above are the classical ones. The Proposition is in a file named `ValOfPowAssociated.lean` ([line 315](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ValOfPowAssociated.lean#L315)), a name that does not match it. Its proof uses `norm_ring` and `trace_ring`, both under `maxHeartbeats 800000`. The second name of the Theorem is proved by `first | exact ...` under `maxHeartbeats 1000000`.
