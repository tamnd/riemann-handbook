---
title: The Euler characteristic in the coprime case
decls:
  - GroundTheory.ProfCoh.finrank_cohomology_alternating_sum_coprime
  - GroundTheory.ProfCoh.eulerChar_coprime
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Euler characteristic in the coprime case

The last two sections prove the local Euler characteristic formula of Tate: for a finite discrete $G_K$-module $M$ of order invertible in $K$,
$$\frac{\# H^0(K, M)\, \# H^2(K, M)}{\# H^1(K, M)} = \frac{1}{\#(\mathcal{O}_K / \# M\, \mathcal{O}_K)}.$$
This section treats the basic case: $M$ is killed by a prime $l$, and $M$ becomes trivial on an open subgroup $V$ whose index is prime to $l$ and whose fixed field contains the $l$-th roots of unity. Then the formula is a computation with Kummer theory over the fixed field of $V$. The next section reduces the general case to this one ([local fields](/learn/galois-cohomology/#local-fields)).

### Discrete modules and the Euler characteristic

Let $K$ be a nonarchimedean local field with ring of integers $\mathcal{O}_K$, let $K^{\mathrm{sep}}$ be a separable closure, and let $G_K = \operatorname{Gal}(K^{\mathrm{sep}}/K)$ with its Krull topology. In this section $K^{\mathrm{sep}}$ carries the valuation that extends the one of $K$. For a closed subgroup $U$ of $G_K$ we write $(K^{\mathrm{sep}})^U$ for its fixed field. If $U$ is open, this is a finite extension of $K$ and again a local field.

**Definition 1.6.1 (discrete module).** Let $H$ be a topological group and $k$ a commutative ring. A $k[H]$-module $M$ is *discrete* if the stabilizer of each $m \in M$ is open in $H$. For a discrete module, $H^i(H, M)$ is the cohomology of the complex of locally constant cochains $H^i \to M$.

Lean: `GroundTheory.ProfCoh.IsDiscreteRep` (also `GroundTheory.ProfCoh.cohomology`).

For a profinite group this is the continuous cohomology of the discrete module $M$ ([continuous cohomology](/learn/galois-cohomology/#continuous-cohomology)). A finite $G_K$-module is discrete if and only if some open subgroup acts trivially on it.

**Definition 1.6.2 (Euler characteristic).** For a discrete module $M$, its *Euler characteristic* is the rational number
$$\chi(H, M) = \prod_{q = 0}^{2} \bigl(\# H^q(H, M)\bigr)^{(-1)^q} = \frac{\# H^0(H, M)\, \# H^2(H, M)}{\# H^1(H, M)},$$
where $\# X$ is the number of elements of $X$ if $X$ is finite and $0$ otherwise, and $0^{-1} = 0$. We write $\chi(M)$ when $H$ is clear.

Lean: `GroundTheory.ProfCoh.eulerChar` (also `GroundTheory.ProfCoh.eulerChar_eq`).

The convention for infinite groups only fixes a value; all theorems below are about cases where the groups are finite. The next theorem says that this holds for $G_K$.

**Theorem 1.6.3 (finiteness and cohomological dimension).** Let $M$ be a finite discrete $G_K$-module whose order is invertible in $K$. Then $H^q(G_K, M)$ is finite for all $q$, and $H^q(G_K, M) = 0$ for $q \geq 3$.

Lean: `GroundTheory.ProfCoh.hasFiniteCohomology_galois_top` (also `GroundTheory.ProfCoh.finite_cohomology_galois_top`, `GroundTheory.ProfCoh.subsingleton_cohomology_galois_top`).

This is the classical result of Serre, *Galois Cohomology*, Chapter II, §5.2 (finiteness) and §5.3 (cohomological dimension $2$). It is proved in the development from local class field theory, and we use it without proof.

### The coprime theorem

Fix a prime $l$ with $l \neq 0$ in $K$. Let $\mu_l \subseteq K^{\mathrm{sep}}$ be the group of $l$-th roots of unity, a $G_K$-module of order $l$. Fix open subgroups $V \leq U$ of $G_K$, and put
$$E = (K^{\mathrm{sep}})^U, \qquad F = (K^{\mathrm{sep}})^V, \qquad \Gamma = U/V.$$
We assume that $V$ is normal in $U$, so $F/E$ is Galois with group $\Gamma$. Let $n \geq 0$ be the integer with $\#(\mathcal{O}_E/l\mathcal{O}_E) = l^n$.

**Example 1.6.4.** If $l$ is different from the residue characteristic $p$, then $l$ is a unit in $\mathcal{O}_E$, and $n = 0$. If $l = p$, then $K$ has characteristic $0$, $E$ is a finite extension of $\mathbb{Q}_p$, and $\#(\mathcal{O}_E/p\mathcal{O}_E) = p^{[E : \mathbb{Q}_p]}$. So $n = [E : \mathbb{Q}_p]$.

**Theorem 1.6.5 (coprime case, dimension form).** Assume that $[U : V]$ is prime to $l$ and that $\mu_l \subseteq F$. Let $M$ be a finite-dimensional discrete $\mathbb{F}_l[U]$-module on which $V$ acts trivially. Then
$$\dim H^0(U, M) - \dim H^1(U, M) + \dim H^2(U, M) = -n \dim M,$$
where all dimensions are over $\mathbb{F}_l$.

Lean: `GroundTheory.ProfCoh.finrank_cohomology_alternating_sum_coprime`.

*Proof.* Step 1 (twisting by $\mu_l$). Let $N = \operatorname{Hom}(\mu_l, M)$, an $\mathbb{F}_l$-vector space of dimension $\dim M$ with an action of $U$. The group $V$ acts trivially on $\mu_l$, since $\mu_l \subseteq F$, and on $M$. So $V$ acts trivially on $N$, and $M \cong \mu_l \otimes N$ as $V$-modules. The Hochschild-Serre spectral sequence for $V \trianglelefteq U$ degenerates, since $\#\Gamma$ is prime to $l$ and $H^j(\Gamma, X) = 0$ for $j > 0$ and $X$ an $\mathbb{F}_l$-module. So restriction gives
$$H^i(U, M) \cong H^i(V, M)^\Gamma \cong \bigl(H^i(V, \mu_l) \otimes N\bigr)^\Gamma,$$
where $\Gamma$ acts on $H^i(V, \mu_l)$ by conjugation.

Step 2 (Kummer theory over $F$). We have $V = \operatorname{Gal}(K^{\mathrm{sep}}/F)$, and as $\Gamma$-modules:
$$\begin{aligned}
H^0(V, \mu_l) &= \mu_l(F) = F^\times[l], \\
H^1(V, \mu_l) &\cong F^\times / (F^\times)^l, \\
H^2(V, \mu_l) &\cong \mathbb{Z}/l\mathbb{Z} \text{ with trivial action}.
\end{aligned}$$
The second line is Kummer theory, from Hilbert's Theorem 90 for $0 \to \mu_l \to (K^{\mathrm{sep}})^\times \xrightarrow{l} (K^{\mathrm{sep}})^\times \to 0$. The third line identifies $H^2(V, \mu_l)$ with the $l$-torsion of the Brauer group of $F$, and the invariant map of $F$ sends it to $\frac{1}{l}\mathbb{Z}/\mathbb{Z}$ compatibly with $\Gamma$.

Step 3 (an additive function). For a finite $\mathbb{F}_l[\Gamma]$-module $X$ put $d(X) = \dim (X \otimes N)^\Gamma$. Since $\#\Gamma$ is prime to $l$, taking $\Gamma$-invariants is exact, so $d$ is additive on short exact sequences. For a $\Gamma$-module $A$ with $A/lA$ and $A[l]$ finite put
$$h(A) = d(A/lA) - d(A[l]).$$
By Steps 1 and 2,
$$\dim H^0(U, M) - \dim H^1(U, M) + \dim H^2(U, M) = d(\mathbb{F}_l) - h(F^\times),$$
where $\mathbb{F}_l$ has the trivial action. Since $F^\times/(F^\times)^l$ is finite for a local field $F$ in which $l \neq 0$, these steps also show that $H^i(U, M)$ is finite for $i \leq 2$.

Step 4 (the units of $F$). We show $h(F^\times) = d(\mathbb{F}_l) + n\, d(\mathbb{F}_l[\Gamma])$, with $\mathbb{F}_l[\Gamma]$ the regular representation. The valuation gives $0 \to \mathcal{O}_F^\times \to F^\times \to \mathbb{Z} \to 0$, and $h$ is additive on such sequences by the snake lemma. Since $h(\mathbb{Z}) = d(\mathbb{F}_l)$, it remains to show $h(\mathcal{O}_F^\times) = n\, d(\mathbb{F}_l[\Gamma])$. The function $h$ does not change when we pass to a $\Gamma$-stable subgroup of finite index. For $k$ large, the group $1 + \mathfrak{m}_F^k$ has no $l$-torsion, and its quotient by $l$-th powers is isomorphic, as a $\Gamma$-module, to $\mathfrak{m}_F^k / l\mathfrak{m}_F^k$. By the normal basis theorem, $\mathfrak{m}_F^k$ contains, with finite index, a lattice $\mathcal{O}_E[\Gamma]\theta \cong \mathcal{O}_E[\Gamma]$. Its quotient by $l$ is $(\mathcal{O}_E/l)[\Gamma] \cong \mathbb{F}_l[\Gamma]^n$, since $\mathcal{O}_E/l\mathcal{O}_E$ has $l^n$ elements. So $h(\mathcal{O}_F^\times) = n\, d(\mathbb{F}_l[\Gamma])$.

Step 5 (conclusion). We have $d(\mathbb{F}_l[\Gamma]) = \dim(\mathbb{F}_l[\Gamma] \otimes N)^\Gamma = \dim N = \dim M$. So the alternating sum is $d(\mathbb{F}_l) - d(\mathbb{F}_l) - n \dim M = -n\dim M$. $\square$

**Corollary 1.6.6 (coprime case).** Under the hypotheses on $l$, $U$ and $V$ of the theorem, let $M$ be a finite discrete $U$-module with $lM = 0$ on which $V$ acts trivially. Then
$$\chi(U, M) = (\# M)^{-n}.$$

Lean: `GroundTheory.ProfCoh.eulerChar_coprime`.

*Proof.* The module $M$ is an $\mathbb{F}_l$-vector space of some dimension $r$, with $\# M = l^r$. The groups $H^i(U, M)$ for $i \leq 2$ are finite, as Step 3 of the last proof shows, so they are $\mathbb{F}_l$-vector spaces with $\# H^i(U, M) = l^{\dim H^i(U, M)}$. By the [Theorem 1.6.5](/entry/finrank-cohomology-alternating-sum-coprime/) in dimension form,
$$\chi(U, M) = l^{\dim H^0 - \dim H^1 + \dim H^2} = l^{-nr} = (\# M)^{-n}. \qquad \square$$

**Remark 1.6.7.** If $l \neq p$ the corollary gives $\chi(U, M) = 1$. If $l = p$ it gives $\chi(U, M) = (\# M)^{-[E:\mathbb{Q}_p]}$, which is Tate's formula over $E$, since $\#(\mathcal{O}_E/\# M\,\mathcal{O}_E) = (\# M)^{[E:\mathbb{Q}_p]}$ for a power $\# M$ of $p$.

**Remark 1.6.8 (Formalization).** The Euler characteristic is defined with `Nat.card`, which is $0$ on an infinite set ([EulerCharDefs.lean](lean:GroundTheory/ProfiniteCohomology/EulerCharDefs.lean#L47)); the finiteness is a separate statement. The coprime theorems take the valuation on $K^{\mathrm{sep}}$ as extra data, through instance arguments, and the normality of $V$ in $U$ is an instance argument. The dimension form needs a raised heartbeat limit ([Coprime.lean](lean:GroundTheory/ProfiniteCohomology/LocalEulerCharacteristic/Coprime.lean#L211)). Step 1 is `GroundTheory.ProfCoh.finrank_cohomology_eq_finrank_invariants`, Step 3 uses `GroundTheory.ProfCoh.AdditiveFunction.invariantsTensor`, and Step 4 is `GroundTheory.ProfCoh.g_units_eq`.
