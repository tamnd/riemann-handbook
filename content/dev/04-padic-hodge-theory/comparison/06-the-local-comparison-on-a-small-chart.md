---
title: The local comparison on a small chart
decls:
  - CrystallineSemistableComparison.B.P.glue
  - CrystallineSemistableComparison.B.P.cont_line
  - CrystallineSemistableComparison.B.local_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The local comparison on a small chart

The crystalline family of the [previous section](/entry/pmap/) is the cohomology of a site of divided power thickenings over $A_{\mathrm{cris}}/\ell^n$. To compare it with étale cohomology, we pass through a second site: the points of the scheme with values in perfectoid algebras. This section proves the local form of that comparison. On a small étale chart of dimension $d$, the pullback from the thickening site to the perfectoid site is an isomorphism on cohomology in degrees up to $j$, up to a fixed power $N$ of $\mu = [\varepsilon] - 1$ (with $\varepsilon$ a compatible system of $\ell$-power roots of unity in the tilt), and $N$ depends only on $d$ and $j$. The proof is in two layers. The first layer is an abstract criterion on cohomology of categories: a torus action, two acyclic "lines" and an equivariant map give the comparison up to a power of $s$. The second layer checks the inputs of the criterion on the chart. The method is close to the local computations on small charts by Bhatt, Morrow and Scholze (*Integral $p$-adic Hodge theory*, Publ. Math. IHÉS 128, 2018). Here we work with the crystalline site and up to bounded torsion. See [[p-adic Hodge theory|6YDZNXR19H]].

All modules in the first layer are over a commutative ring $R$, and $s \in R$.

**Definition 2.6.1 (Maps up to $s$).** A linear map $f : M \to N$ is *injective up to $s$* if $f(x) = 0$ implies $sx = 0$. It is *surjective up to $s$* if for each $y \in N$ there is $x$ with $f(x) = sy$. It is an *isomorphism up to $s$* if it is both. A complex is *exact up to $s$* at a term if $s$ kills the cohomology there in the same sense.

**Definition 2.6.2 (Cohomology of a category).** Let $F : \mathcal{C} \to \mathrm{Mod}_R$ be a functor. Its cohomology $H^j(\mathcal{C}, F)$ is the cohomology of the complex whose term of degree $n$ is the product of $F(T_n)$ over all chains $T_0 \to T_1 \to \cdots \to T_n$ in $\mathcal{C}$. These are the derived functors of the limit. A functor $G : \mathcal{C}' \to \mathcal{C}$ gives a restriction map $H^j(\mathcal{C}, F) \to H^j(\mathcal{C}', F \circ G)$. We say that *$G$ restricts isomorphically up to $s$ in degrees $\leq n$* if this map is an isomorphism up to $s$ for every $j \leq n$.

**Definition 2.6.3 (Descent up to $s$).** A functor $G : \mathcal{C}' \to \mathcal{C}$ has *descent up to $s$* for $F$ if for each object $T$ of $\mathcal{C}$ the augmented complex
$$0 \to F(T) \to C^\bullet\big(T \downarrow G,\ F \circ G\big)$$
is exact up to $s$ in every degree. Here $T \downarrow G$ is the category of maps $T \to G(T')$, and $C^\bullet$ is the complex of the previous definition.

**Definition 2.6.4 (Torus action and line).** Let $\Gamma_d = \mathbb{N}^d$, written multiplicatively, with generators $g_1, \ldots, g_d$. Let $U$ be a functor from $\mathcal{C}$ to abelian groups with a natural element $q \in U(T)$, and let $j : \mathcal{C}_0 \to \mathcal{C}$ be full and faithful.

1. A *torus action* on an object $D$ is an action of tuples $a \in U(T)^d$ on the set of maps $D \to T$, natural in $T$, such that maps $D \to j(t)$ exist and the action on them is simply transitive. The tuple $(q^{a_1}, \ldots, q^{a_d})$ then gives an action of $\Gamma_d$ on $D$.
2. A *line* is an endofunctor $\Xi$ of $\mathcal{C}$ with a natural map $i : T \to \Xi(T)$, an element $\eta \in U(\Xi(T))$ and an endomorphism $\gamma$ of $\Xi$, such that $\gamma i = i$, $\gamma(\eta) = q\eta$, and such that maps $\Xi(T) \to j(t)$ correspond to a map $T \to j(t)$ together with an element of $U(j(t))$, the image of $\eta$.
3. The line is *acyclic up to $s$* for $F$ if for each $T$: the map $F(i)$ is injective up to $s$; each fixed point $x$ of $F(\gamma)$ has $sx$ in the image of $F(i)$; and each $sx$ has the form $F(\gamma)y - y$.

So a line is an abstract form of "functions on $\mathbb{Z}$ with the shift", and acyclicity says that its cohomology for the shift is the constants, up to $s$.

**Definition 2.6.5 (Splitting up to $s$).** Let $\alpha : M \to N$ be a map of $R$-modules with an action of $\Gamma_d$. A *splitting up to $s$* of $\alpha$ consists of $\Gamma_d$-equivariant maps: a retraction $r$ with $r\alpha = 1$ and orthogonal idempotents $\pi_1, \ldots, \pi_d$ on $N$ with $\pi_k \alpha = 0$ and $\alpha r + \sum_k \pi_k = 1$, such that on the image of $\pi_k$ the map $g_k - 1$ is injective up to $s$ and surjective up to $s$ onto the image of $\pi_k$.

A splitting says that $N$ is $M$ plus pieces on which some generator acts without fixed points, up to $s$. On each such piece the group cohomology of $\Gamma_d$ is killed by $s^2$.

**Lemma 2.6.6 (The gluing criterion).** For all $d$ and $n$ there is $N$ with the following property. Let $F : \mathcal{C} \to \mathrm{Mod}_R$, $G : \mathcal{E} \to \mathcal{C}$, and $j : \mathcal{E}_0 \to \mathcal{E}$ full and faithful. Assume:

1. an object $D$ of $\mathcal{C}$ has a torus action (with $j$ the identity), and $\mathcal{C}$ has a line that is acyclic up to $s$ for $F$;
2. an object $D'$ of $\mathcal{E}$ has a torus action relative to $j$, and $\mathcal{E}$ has a line that is acyclic up to $s$ for $F \circ G$;
3. $j$ has descent up to $s$ for $F \circ G$;
4. there is a map $\theta : D \to G(D')$ that commutes with the two actions of $\Gamma_d$, and $F(\theta)$ has a splitting up to $s$.

Then $G \circ j$ restricts isomorphically up to $s^N$ in degrees $\leq n$ for $F$.

Lean: `CrystallineSemistableComparison.B.P.glue`.

*Proof.* Let $\Gamma_d \to \mathcal{C}$ and $\Gamma_d \to \mathcal{E}$ be the one-object functors given by the actions on $D$ and $D'$. We take as given the following fact on torus actions: if a torus action on $D$ is simply transitive relative to $j$, $j$ has descent up to $s$, and a line is acyclic up to $s$, then the restriction to $\Gamma_d$ is an isomorphism up to $s^{N_1}$ in degrees $\leq n$, with $N_1$ depending only on $d$ and $n$. The idea is that the line resolves each object by $\Gamma_d$-translates, so that the cohomology of the category becomes the Koszul cohomology of $\Gamma_d$ on $F(D)$.

1. Apply it to $\mathcal{C}$ with $j$ the identity. The identity has descent up to $s$, because $T \downarrow \mathrm{id}$ has an initial object. We get an isomorphism $H^\bullet(\mathcal{C}, F) \to H^\bullet(\Gamma_d, F(D))$ up to $s^{N_1}$.
2. Apply it to $\mathcal{E}$, $F \circ G$ and $j$, with hypothesis 3. We get an isomorphism $H^\bullet(\mathcal{E}, F \circ G) \to H^\bullet(\Gamma_d, F(G(D')))$ up to $s^{N_2}$.
3. The map $F(\theta)$ has a splitting up to $s$. So it induces an isomorphism $H^\bullet(\Gamma_d, F(D)) \to H^\bullet(\Gamma_d, F(G(D')))$ up to $s^2$. The square formed by the restriction to $\Gamma_d$ through $D$, through $D'$ and by $\theta$ commutes on cohomology. So the restriction $H^\bullet(\mathcal{C}, F) \to H^\bullet(\Gamma_d, F(G(D')))$ is an isomorphism up to $s^{N_1 + 2}$.
4. By steps 2 and 3, and the rule "if $u$ and $vu$ are isomorphisms up to $s$ and $s'$, then $v$ is one up to $ss'$", the restriction along $G$ is an isomorphism up to $s^{N_2 + N_1 + 2}$.
5. Hypothesis 3 also gives that $j$ restricts isomorphically up to $s^{2n+3}$ in degrees $\leq n$ for $F \circ G$. This is a comparison of a cohomology of a category with the cohomology of a full subcategory, by the augmented complexes of the definition of descent.
6. Compose steps 4 and 5. The restriction along $G \circ j$ is an isomorphism up to $s^N$ with $N = N_2 + (N_1 + 2) + (2n + 3)$. $\square$

Now we turn to the chart. Fix a prime $\ell$ and units $\varepsilon_0, \varepsilon_1, \ldots$ of the tilt $\mathcal{O}_{\mathbb{C}_\ell}^\flat$ with $\varepsilon_{m+1}^\ell = \varepsilon_m$, $\varepsilon_0^\sharp = 1$ and $\varepsilon_1^\sharp \neq 1$. So $\varepsilon_0$ is the element $\varepsilon = (1, \zeta_\ell, \zeta_{\ell^2}, \ldots)$ of the tilt. Put $q = [\varepsilon_0] \in A_{\mathrm{inf}}$ and $\mu = q - 1$.

**Definition 2.6.7 (Small chart and the two sites).** Let $O$ be a ring with a map $\kappa : O \to \mathcal{O}_{\mathbb{C}_\ell}$, and let $F$ be a functor of points over $O$.

1. $F$ is *small of dimension $d$* if $F$ is represented by an $O$-algebra $R$, with a universal point over $R$, and $R$ has units $T_1, \ldots, T_d$, such that $O[T_1, \ldots, T_d] \to R$ is étale.
2. The *thickening site* over $A_{\mathrm{cris}}/\ell^n$ has as objects the divided power thickenings of points of $F$ over $A_{\mathrm{cris}}/\ell^n$. A Boolean flag $k$ selects one of two divided power bases. Let $\mathcal{O}$ be its structure functor.
3. A function $\rho : \mathbb{N} \to \mathbb{N}$ is *slow* if $\rho(0) = 0$ and $\rho(r + 1) \leq \rho(r) + 1$. Put $\mathrm{Fil}^r \mathcal{O} = I^{[\rho(r)]}$, the $\rho(r)$-th divided power ideal of the thickening. Since $\mu \in I$ and $\rho$ is slow, $\mu \cdot \mathrm{Fil}^r \subseteq I^{[\rho(r) + 1]} \subseteq \mathrm{Fil}^{r+1}$. Its *Rees module* is $\prod_r \mathrm{Fil}^r \mathcal{O}$ over $\mathbb{Z}[X]$, where $X$ sends the component $r$ to $\mu$ times it in the component $r + 1$.
4. The *perfectoid site* has as objects the test perfect $\mathcal{O}_{\mathbb{C}_\ell}^\flat$-algebras $A$ (complete, algebraically closed, and of valuation type) with a point of $F$ over the untilt $A^\sharp$ that lies over $\kappa$. The functor $g$ sends such an object to the thickening $A_{\mathrm{cris}}(A)/\ell^n \to A^\sharp$.

**Lemma 2.6.8 (The line of continuous functions).** Let $O$, $F$, $\kappa$ and $\varepsilon$ be as above, $k$ a flag, $n \geq 0$ and $\rho$ slow. Take for $U(A)$ the units $u$ of $A$ with $u^\sharp = 1$, with $\varepsilon_0$ as the element $q$. Then the site of all perfect algebras with a point of $F$ has a line relative to the inclusion of the perfectoid site that is acyclic for the filtration $\mathrm{Fil}^\bullet \mathcal{O}$ pulled back by $g$, in the filtered sense: $i$ is injective; if $\gamma x = x$ with $x \in \mathrm{Fil}^r$, then $\mu x = i(m)$ with $m \in \mathrm{Fil}^{r+1}$, and each $\mu x$ with $x \in \mathrm{Fil}^r$ has the form $\gamma y - y$ with $y \in \mathrm{Fil}^{r+1}$.

Lean: `CrystallineSemistableComparison.B.P.cont_line` (a second name for `GlobalTheory.CompanionTheory.ContLine.exists_line`).

*Proof.* Let $\Xi(A)$ be the algebra of continuous functions $\mathbb{Z}_\ell \to A$, let $i$ be the constant functions, let $\gamma$ be the translation by $1$, and let $\eta$ be the function $z \mapsto \varepsilon_0^z$, so that $\eta^\sharp = 1$ and $\gamma(\eta) = \varepsilon_0 \eta$. The acyclicity is the [Theorem 1.3.7 of Volume 3](/entry/exists-line/) on the line of continuous functions, which we take as given here. The universal property of the line comes from the universal property of continuous functions on $\mathbb{Z}_\ell$: a map from $\Xi(A)$ to a test algebra is a map from $A$ together with the image of $\eta$. $\square$

In the Rees module, the filtered acyclicity of the lemma is acyclicity up to $X$, so the line is acyclic up to $X$ in the sense of the gluing criterion.

**Theorem 2.6.9 (Local comparison on a small chart).** Assume the descent statement for perfect algebras: the functors $(W(A)/\xi)/\ell^n$, $A_{\mathrm{cris}}(A)/\ell^n$ and $\mathrm{Fil}^r A_{\mathrm{cris}}(A)/\ell^n$ have descent to test algebras up to each element of $W(\mathfrak{m}^\flat)$. Then for all $d$ and $j$ there is $N$ such that the following holds. Let $O$ be a ring, $F$ a functor of points over $O$ that is small of dimension $d$, $\kappa : O \to \mathcal{O}_{\mathbb{C}_\ell}$, $\varepsilon$ a system of roots as above, $n \neq 0$, $\rho$ slow, and $k$ a flag with $k$ false or $\rho = 0$. Then the functor $g$ from the perfectoid site to the thickening site restricts isomorphically up to $X^N$ in degrees $\leq j$ for the Rees module of $\mathrm{Fil}^\bullet \mathcal{O}$.

Lean: `CrystallineSemistableComparison.B.local_of`.

*Proof.* Take $N$ from the [gluing criterion](/entry/glue/) for $d$ and $j$. Fix $F$, $\kappa$, $\varepsilon$, $k$, $n$ and $\rho$, and let $R$, $T_1, \ldots, T_d$ be the chart.

1. *Lift of the chart.* Since $O[T_1, \ldots, T_d] \to R$ is étale, it lifts to an étale algebra $\tilde{R}$ over the divided power base $A_{\mathrm{cris}}/\ell^n$, with lifts $t_k$ of the $T_k$. The lift is flat, so the divided powers extend to $\tilde{R}$. This gives an object $D$ of the thickening site.
2. *Tower.* There is a test perfect algebra with compatible $\ell$-power roots $c_k(m)$ of the $T_k$: $c_k(m+1)^\ell = c_k(m)$ and $c_k(0)^\sharp = T_k$. It is universal for such systems of roots. This gives an object $D'$ of the perfectoid site.
3. *Actions.* The group $\Gamma_d$ acts on $D$ by $t_k \mapsto q^{a_k} t_k$, and on $D'$ by $c_k \mapsto \varepsilon_0^{a_k} c_k$. Both are torus actions in the sense above. On the thickening side $U(T)$ is the group of units $u$ with $u - 1$ in the ideal of the thickening, and on the perfectoid side it is the group of units with $u^\sharp = 1$.
4. *The map $\theta$.* There is a map $\theta : D \to g(D')$ with $\theta(t_k) = [c_k(0)]$ that commutes with the two actions.
5. *Lines.* On the thickening site a line comes from a universal construction and is acyclic up to $X$. This uses $q = [\varepsilon_1]^\ell$, $\mu = q - 1$, and that $\sum_{i < \ell} [\varepsilon_1]^i$ lies in the first divided power ideal. On the perfectoid site the line is the line of continuous functions of the [lemma](/entry/cont-line/).
6. *Splitting.* Since $n \neq 0$, the map $\mathcal{O}(\theta)$ on Rees modules has a splitting up to $X$. The pieces $\pi_k$ are the parts of non-integral exponent in $c_k$, on which $g_k - 1$ is invertible up to $\mu$.
7. *Descent.* By the hypothesis, and since $k$ is false or $\rho = 0$, the inclusion of the perfectoid site into the site of all perfect algebras has descent up to $X$ for the pulled back Rees module.

Steps 1 to 7 are the hypotheses of the gluing criterion with $s = X$, $\mathcal{C}$ the thickening site, $\mathcal{E}$ the site of all perfect algebras, and $j$ the inclusion of the perfectoid site. The criterion gives the claim. $\square$

**Remark 2.6.10 (Formalization).** The theorem is `local_of` in [SubsingletonH.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/ZariskiEtaleLifting/SubsingletonH.lean#L32), whose name has nothing to do with subsingletons; its conclusion is the definition `Local`, and its hypothesis is `D.Out`, proved later in this chapter ([Theorem 2.8.11](/entry/out/)). The criterion is in [FGlue.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/ZariskiEtaleLifting/FGlue.lean#L44), and the fact on torus actions in its proof is `P.tors`. The lemma `P.cont_line` is a second name, and like the inputs `P.elift`, `P.tower_ex`, `P.tower_act` and `P.theta_ex` of steps 1 to 4 its proof is under `Development/AutomorphicSpectrum/Proofs/BlockDecomposition`, a folder name with no relation to this content. Step 6 follows the statement of `P.local_ni` only; we did not read its proof, and "non-integral exponent" describes the usual argument.
