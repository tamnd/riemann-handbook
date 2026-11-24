---
title: Local densities and the local mass of a type
decls:
  - PI.UnitaryGroupMassFormula.LocDensCorank.fieldCount_holds
  - PI.UnitaryGroupMassFormula.LocDensCorank.fld_count_core
  - PI.LocMassTypW.local_mass_type_of_parts
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Local densities and the local mass of a type

The mass formula is a product of local factors. This section computes two of them. At a place where the quadratic extension is a field, the local density of a diagonal form against a self-dual lattice is an explicit product, found by counting over the residue field. At a place that splits, the orbit measure of the pairs of tuples of a given type is a ratio of volumes of compact open subgroups. The two results are the theorem on [local densities by corank](/entry/local-density-corank/) and the theorem on the [local mass of a type](/entry/loc-mass-typ/) of the chapter on orbital bounds. For the classical background see [local densities](/learn/hermitian-lattices/#local-densities).

### Hermitian lattices over a local field

Let $F$ be a nonarchimedean local field with ring of integers $\mathcal{O}_F$ and residue field $k_F$ of order $q$. Let $E$ be a commutative $F$-algebra of rank $2$ with an $F$-linear involution $x \mapsto \bar x$ whose fixed ring is $F$. Let $\mathcal{O}_E$ be the integral closure of $\mathcal{O}_F$ in $E$. We assume that $E$ is unramified in this sense: for every irreducible $\varpi \in \mathcal{O}_F$ and $x \in \mathcal{O}_E$, if $x^2 \in \varpi \mathcal{O}_E$ then $x \in \varpi \mathcal{O}_E$. (See [places and completions](/learn/number-fields/#places-and-completions).)

Let $V$ be a free $E$-module of finite rank $n$ with a nondegenerate Hermitian form $h$, linear in the first variable. A *lattice* $\Lambda \subseteq V$ is a finitely generated $\mathcal{O}_E$-submodule that spans $V$. It is *self-dual* if $x \in \Lambda$ exactly when $h(x, y) \in \mathcal{O}_E$ for all $y \in \Lambda$. A family $v = (v_a)_{a \in I}$ in $V$ is *primitive* for $\Lambda$ if all $v_a$ lie in $\Lambda$, the family is linearly independent over $E$, and every $x \in \Lambda$ in the $E$-span of $v$ lies in its $\mathcal{O}_E$-span.

**Definition 7.4.1 (Local density).** Let $\varpi$ be irreducible in $\mathcal{O}_F$, $I$ a finite set of size $m$ and $G$ an $I \times I$ matrix over $E$. The *local density* of $G$ for $\Lambda$ is
$$\delta_\Lambda(G) = \frac{\# \{ v \bmod \varpi \Lambda : v \text{ primitive},\ h(v_b, v_a) - G_{ab} \in \varpi \mathcal{O}_E \text{ for all } a, b \}}{q^{2nm - m^2}}.$$

The numerator counts the images in $(\Lambda / \varpi\Lambda)^I$ of primitive families whose Gram matrix is congruent to $G$ modulo $\varpi$. The denominator is $q$ to the power $\dim_F$ of the tuples minus $\dim_F$ of the Hermitian $m \times m$ matrices: it is the factor that makes the count a density of a fibre of the Gram map.

**Definition 7.4.2 (Product of local factors).** For $q, n, m, c \in \mathbb{N}$ and $\eta \in \mathbb{R}$ put
$$P_\eta(q; n, m, c) = \prod_{i = \max(n + 1 - m - c,\, 0)}^{n} \big(1 - \eta^i q^{-i}\big).$$

When $m + c \leq n$ the product has $m + c$ factors. When $m + c > n$ it contains the factor with $i = 0$, which is $0$.

### The density at an inert place

**Theorem 7.4.3 (Local density of a diagonal form).** Let $F$ have characteristic $0$, and let $E$ be as above with every nonzero element of $E$ a unit, so that $E$ is the unramified quadratic field extension of $F$. Let $\Lambda$ be a self-dual lattice in $V$ of rank $n$, let $\varpi \in \mathcal{O}_F$ be irreducible, and let $a = (a_i)_{i \in I}$ be a family in $\mathcal{O}_F$ with $|I| \leq n$. Let $c$ be the number of $i$ with $\varpi \mid a_i$. Then
$$\delta_\Lambda(\operatorname{diag}(a)) = P_{-1}(q; n, |I|, c).$$

Lean: `PI.UnitaryGroupMassFormula.LocDensCorank.fieldCount_holds`.

The proof reduces to a count over finite fields, which we take as given. It is proved elsewhere in the development.

**Theorem 7.4.4 (Hermitian count over a finite field).** Let $k$ be a field of order $q^2$ that contains the field $k_0$ of order $q$. Let $\Phi$ be an invertible $n \times n$ matrix over $k$ with $\Phi_{lk} = \Phi_{kl}^q$, and $G$ an $m \times m$ matrix over $k$ with $G_{ji} = G_{ij}^q$. Let $N$ be the number of linearly independent families $X_1, \dots, X_m \in k^n$ with $\sum_{k, l} X_{i k} \Phi_{kl} X_{j l}^q = G_{ij}$ for all $i, j$. Then
$$\frac{N}{q^{2nm - m^2}} = P_{-1}(q; n, m, m - \operatorname{rank} G).$$

The main step is a version of the theorem for one fixed basis.

**Lemma 7.4.5 (Density from a basis).** Let $F$ and $E$ be as in the setting above, and $\varpi \in \mathcal{O}_F$ irreducible. Assume:

1. for every $x \in E$ there is a nonzero $c \in \mathcal{O}_F$ with $c x \in \mathcal{O}_E$;
2. every nonzero $x \in \mathcal{O}_E$ is $\varpi^j u$ for some $j \geq 0$ and some unit $u$ of $\mathcal{O}_E$;
3. there is a finite field $k$ with $|k| = q^2$ and a surjective ring map $\rho : \mathcal{O}_E \to k$ with kernel $\varpi \mathcal{O}_E$ and $\rho(\bar x) = \rho(x)^q$;
4. $\Lambda$ is self-dual, and $b_1, \dots, b_n$ is a family in $\Lambda$, linearly independent over $E$, such that every element of $\Lambda$ is an $\mathcal{O}_E$-combination of the $b_k$;
5. there is a matrix $Q$ over $\mathcal{O}_E$ with $Q \cdot (h(b_k, b_l))_{k,l} = 1$.

Then for every finite family $a = (a_i)_{i \in I}$ in $\mathcal{O}_F$, with $c$ the number of $i$ with $\varpi \mid a_i$,
$$\delta_\Lambda(\operatorname{diag}(a)) = P_{-1}(q; n, |I|, c).$$

Lean: `PI.UnitaryGroupMassFormula.LocDensCorank.fld_count_core`.

*Proof.* Write $v_a = \sum_k X_{ak} b_k$ with $X_{ak} \in \mathcal{O}_E$, and reduce by $\rho$. By hypotheses 1, 2 and 4, a family $v$ in $\Lambda$ is primitive exactly when the reduced family $\rho(X)$ is linearly independent over $k$, and two families have the same image modulo $\varpi \Lambda$ exactly when they have the same reduction. The Gram condition $h(v_b, v_a) \equiv a_a \delta_{ab}$ modulo $\varpi$ becomes, by hypothesis 3,
$$\sum_{k,l} \rho(X)_{b k}\, \Phi_{kl}\, \rho(X)_{a l}^q = \rho(a_a) \delta_{ab}, \qquad \Phi_{kl} = \rho\big(h(b_k, b_l)\big).$$
So the numerator of $\delta_\Lambda$ is the number $N$ of the Hermitian count, with this $\Phi$ and $G = \operatorname{diag}(\rho(a_i))$. The matrix $\Phi$ is invertible by hypothesis 5, and $\Phi_{lk} = \Phi_{kl}^q$ because $h$ is Hermitian and $\rho$ turns the involution into the $q$-th power. The image of $\mathcal{O}_F$ in $k$ is a subfield of order $q$, and $k$ has dimension $2$ over it. The rank of $G$ is the number of $i$ with $\rho(a_i) \neq 0$, that is $|I| - c$. The Hermitian count over a finite field gives the result. $\square$

*Proof of the theorem.* For $F$ of characteristic $0$ and $E$ a field, hypotheses 1 and 2 are integrality properties of the local ring $\mathcal{O}_E$, and the residue field $\mathcal{O}_E / \varpi \mathcal{O}_E$ is a field of order $q^2$ on which the involution acts as the $q$-th power, since $E$ is unramified. A self-dual lattice has an $\mathcal{O}_E$-basis, since $\mathcal{O}_E$ is a principal ideal domain, and its Gram matrix is invertible over $\mathcal{O}_E$ by self-duality. These are proved lemmas. The lemma above then gives the result. $\square$

The bound $|I| \leq n$ is not needed in the lemma: when $|I| > n$ there are no linearly independent families, and the product contains the factor $1 - 1 = 0$.

### The local mass of a type at a split place

Now let $F$ be a number field and $E$ a CM quadratic extension with involution $\sigma$, $J$ a nondegenerate Hermitian matrix of size $n$ over $E$, and $\psi$ a standard additive character of the adeles of $F$. Let $U$ be the unitary group of $J$. Fix a finite place $v$ of $F$ that splits in $E$, so that $E_v = F_v \otimes_F E$ has an idempotent other than $0$ and $1$, and that is unramified in $E$. Let $g$ be a prime number with $v \mid g$ and with absolute norm of $v$ equal to $g$.

Let $\Lambda$ be an $\mathcal{O}_E$-lattice in $E^n$ whose completion $\Lambda_v$ is self-dual for $J$. Let $K_v \subseteq U(F_v)$ be the stabilizer of $\Lambda_v$, and $K_{g,v} \subseteq K_v$ the subgroup of elements $x$ with $(x - 1)\Lambda_v \subseteq g \Lambda_v$.

A *frame* $P$ is an $(r+1)$-tuple of vectors in $E^n$ of the standard shape with value $T \in F$, as in the chapter on orbital bounds. Attached to $P$ are a closed subgroup $S_P \subseteq U(F_v)$, a subgroup $S^0_P \subseteq S_P$, and a family of unipotent elements of $S_P$ parametrized by a product $\mathcal{U}$ of copies of $E_v$. A tuple $X$ is rescaled to $\ell X$ with $(\ell X)_a = d^{-(r-a)} X_a$ for $a < r$ and $(\ell X)_r = X_r$, where $d$ is a fixed element of $F_v$ attached to the different of $F$. Let $\omega_T$ be the orbit measure on tuples with Gram matrix $T$. Put
$$\Omega_g = \{ (X, X') : \ell X, \ell X' \text{ primitive for } \Lambda_v,\ \ell X' - \ell X \in g \Lambda_v^{r+1} \},$$
and let $K^\natural_v = \{ x \in K_v : x = s \kappa,\ s \in S_P \cap K_v,\ \kappa \in K_{g,v} \}$. Let $\mathcal{U}_{\mathcal{O}} \subseteq \mathcal{U}$ be the integral points (with the same rescaling), $\mathcal{U}_g$ the pairs in $\mathcal{U}_{\mathcal{O}} \times \mathcal{U}_{\mathcal{O}}$ that are congruent modulo $g$ after rescaling, and $\operatorname{vol}$ the self-dual measure for $\psi_v$ on $\mathcal{U}$.

We say that a Haar measure $\mu_S$ on $S_P$ is *tied* to a Haar measure $\mu_G$ on $U(F_v)$ if there is a Haar measure $\mu^0$ on $S^0_P$ such that $\mu_G = \mu^0 \cdot \omega_{T_P}$ (the quotient measure on the orbit of $P$ is $\omega_{T_P}$) and $\mu_S = \mu^0 \times \operatorname{vol}$ on $S_P = S^0_P \cdot \mathcal{U}$.

We take two statements as given; each is proved elsewhere in the development, and the [theorem](/entry/loc-mass-typ/) that uses the result below supplies them.

**Theorem 7.4.6 (Right invariance under the maximal compact).** Under the hypotheses above, every Haar measure $\mu_G$ on $U(F_v)$ satisfies $\mu_G(A \kappa) = \mu_G(A)$ for all measurable $A$ and $\kappa \in K_v$.

**Theorem 7.4.7 (Integral unipotents).** Under the hypotheses above, for every $u \in \mathcal{U}_{\mathcal{O}}$ there is $s \in K_v$ that acts on the vectors of $P$ by the unipotent matrix of $u$.

**Theorem 7.4.8 (Local mass of a type).** Assume the two theorems above. Let $P$ and $P'$ be frames with values $T$ and $T'$, with $\ell P$ and $\ell P'$ primitive for $\Lambda_v$, and assume that there is $\kappa \in K_v$ with $\kappa \cdot \ell P' - \ell P \in g \Lambda_v^{r+1}$. Let $\mu_G$ be a Haar measure on $U(F_v)$, and $\mu_S$, $\mu_{S'}$ Haar measures on $S_P$, $S_{P'}$ tied to $\mu_G$. Then
$$\frac{(\omega_{T} \times \omega_{T'})(\Omega_g)}{\operatorname{vol}(\mathcal{U}_g)} = \frac{\mu_G(K_v)\, \mu_G(K^\natural_v)}{\mu_S(S_P \cap K_v)\, \mu_{S'}(S_{P'} \cap K_v)}.$$

Lean: `PI.LocMassTypW.local_mass_type_of_parts`.

*Proof.* There are four inputs, each a proved lemma except where the two given theorems enter.

First, the volume of the integral points of $S_P$ factors: $\mu_S(S_P \cap K_v) = \mu^0(S^0_P \cap K_v) \cdot \operatorname{vol}(\mathcal{U}_{\mathcal{O}})$. This uses the theorem on integral unipotents, which shows that $S_P \cap K_v$ is the product of $S^0_P \cap K_v$ and the integral unipotents. The same holds for $P'$. The factor $\mu^0(S^0_P \cap K_v)$ is nonzero.

Second, the orbit measure of $\Omega_g$ is computed. At a split place $U(F_v) \cong GL_n(F_v)$; the lattice is standard after a change of basis, and $K_v$ acts transitively on the primitive tuples of a given type. Unfolding $\omega_T \times \omega_{T'}$ with the tie of measures, and using the right invariance of $\mu_G$ under $K_v$, expresses $(\omega_T \times \omega_{T'})(\Omega_g)$ as a ratio of $\mu_G(K_v) \mu_G(K^\natural_v)$ to $\mu^0(S^0_P \cap K_v) \mu^0(S^0_{P'} \cap K_v)$, up to the unipotent volumes.

Third, an index formula, which again uses integral unipotents, relates $\operatorname{vol}(\mathcal{U}_g)$ to $\operatorname{vol}(\mathcal{U}_{\mathcal{O}})^2$.

Fourth, a separate identity expresses the volumes of the unipotent sets in terms of $g$ and $r$, and these volumes are positive. Putting the four together and cancelling gives the formula. $\square$

**Remark 7.4.9 (Formalization).** The density lemma does not assume characteristic $0$ or $|I| \leq n$. The theorem asks for $|I| \leq n$, and its proof does not use that hypothesis: see [FieldCountHolds.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LocalDensityCorank/FieldCountHolds.lean#L155), where it is the last, unnamed, argument. The condition that $v$ splits is stated as the existence of a nontrivial idempotent in $F_v \otimes_F E$. The groups $S_P$ and $S^0_P$, the parametrization of the unipotents, the orbit measures, and the lemmas of the second, third and fourth steps of the proof of the local mass were not unfolded; the text gives what their statements say. The density statements are in [SplitCount.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LocalDensityCorank/SplitCount.lean#L21) and the local mass in [LocalMassTypeOfParts.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/LocalMassType/LocalMassTypeOfParts.lean#L76), with the statement in [LocVol.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/LocVol.lean#L303).
