---
title: De Rham Hecke characters
decls:
  - PositivityTheory.SecR.Hladr.lubinTate_at_embedding
  - PositivityTheory.SecR.Hladr.field_of_ltPeriods
  - PositivityTheory.SecR.Hladr2.field_of_leaves
status: drafted
drafted_by: writer@claude-opus-5-5
---
## De Rham Hecke characters

Let $\chi$ be an algebraic [[Hecke character|KPYFGB342X]] of a number field $E$ with infinity type $n$, and let $\mu$ be its $l$-adic Galois character. This section proves that the restriction of $\mu$ to a decomposition group above $l$ is de Rham, with the single Hodge-Tate jump $-n(\iota \circ \tau)$ at each embedding $\tau$ of $E$. The proof writes $\mu$ near $w$ as a product of powers of Lubin-Tate characters, one for each embedding of $E_w$, times a character that is trivial on an open subgroup of inertia. The Lubin-Tate characters are de Rham with known jumps by [the theorem on periods](/entry/has-periods-main/) of the previous section. The result is used by [the unconditional form](/entry/field-outright/) in the step [every character of the literature](/step/every-character-of-literature/).

### The setting

Let $E$ be a number field, $\Omega$ an algebraic closure of $E$, $G_E = \mathrm{Gal}(\Omega/E)$, and $G_E^{\mathrm{ab}}$ its topological abelianization. Let $\mathbb{I}_E$ be the idele group. A *global Artin map* is a homomorphism $\mathrm{art} : \mathbb{I}_E \to G_E^{\mathrm{ab}}$ that is an open quotient map, whose kernel is the closure of $E^\times$ times the identity component at infinity, which maps the local units at a finite place $v$ onto the image of inertia, which maps the uniformizers at $v$ to the inverses of Frobenius elements, and which maps the closure of the image of $E_v^\times$ onto the image of the decomposition group. These are the properties of the reciprocity map of [Hecke characters](/learn/class-field-theory/#hecke-characters) in the geometric normalization. A *Hecke character* is a continuous homomorphism $\chi : \mathbb{I}_E \to \mathbb{C}^\times$ that is trivial on $E^\times$. Write $\chi_\infty(k)$ for the value of $\chi$ at the idele with components $k$ at the infinite places and $1$ at the finite places.

**Definition 4.8.1 (Algebraic Hecke character).** Let $n : \mathrm{Hom}(E, \mathbb{C}) \to \mathbb{Z}$. A Hecke character $\chi$ is *algebraic of type $n$* if $\chi_\infty(k) = \prod_{\varphi} \varphi(k)^{n(\varphi)}$ for each $k \in E^\times$ that is positive at all real embeddings.

**Definition 4.8.2 (The $l$-adic character).** Let $l$ be a prime, $\bar{\mathbb{Q}}_l$ an algebraic closure of $\mathbb{Q}_l$, and $\iota : \bar{\mathbb{Q}}_l \to \mathbb{C}$ a field isomorphism. A homomorphism $\mu : G_E \to \bar{\mathbb{Q}}_l^\times$ is the *$l$-adic character of $(\chi, n)$* if for each idele $x$ and each $\sigma \in G_E$ with $\mathrm{art}(x) = \sigma^{\mathrm{ab}}$,
$$\mu(\sigma) = \iota^{-1}\bigl(\chi(x)\, x_\infty^{-n}\bigr) \cdot \prod_{v} \prod_{j} j(x_v)^{n(\iota \circ j|_E)},$$
where $x_\infty^{n} = \prod_{u \mid \infty} \prod_{i} i(x_u)^{n(i|_E)}$ over the continuous embeddings $i : E_u \to \mathbb{C}$, and $j$ runs over the continuous embeddings $E_v \to \bar{\mathbb{Q}}_l$ at the finite places $v$.

Only the places $v$ above $l$ have such embeddings. Now fix a finite place $w$ of $E$ and a valuation ring $A$ of $\Omega$ above $w$, with decomposition group $D_A$ and inertia group $I_A$. A *local bridge* at $A$ consists of a finite extension $K_w$ of $\mathbb{Q}_l$ in $\bar{\mathbb{Q}}_l$, a ring map $j : \Omega \to \bar{\mathbb{Q}}_l$ that maps $E$ to a dense subset of $K_w$, and an isomorphism of topological groups $e : D_A \to G_{K_w}$ with $e(g)(j(x)) = j(g x)$. It also fixes a finite extension $L$ of $\mathbb{Q}_l$ that contains the images of all embeddings of $K_w$, and an identification of a ring $O$ with $O_L$. The bridge *induces* $A$ if $A = \{x \in \Omega : |j(x)| \leq 1\}$. An embedding $\tau' : K_w \to L'$ *induces* $\tau : E \to \bar{\mathbb{Q}}_l$ if $\tau(x) = \tau'(j(x))$ for $x \in E$.

For a character $\psi : D_A \to L'^\times$ with $L \subseteq L'$, the bridge makes $\psi \circ e^{-1}$ a character of $G_{K_w}$ with coefficients in $L'$. Given a period datum $P$ at $l$ (as in [the previous section](/entry/has-periods-main/)), $\psi$ is *de Rham* if $D_{\mathrm{dR}}(\psi) = (L' \otimes B_P)^{G_{K_w}}$ has $L'$-dimension $[K_w : \mathbb{Q}_l]$. Its *jump multiplicity* at an embedding $\tau' : K_w \to L'$ and $a \in \mathbb{Z}$ is $\dim \mathrm{Fil}^a_{\tau'} - \dim \mathrm{Fil}^{a+1}_{\tau'}$ for the $\tau'$-part of the filtration of $D_{\mathrm{dR}}(\psi)$. For a function $J$ on embeddings, $\psi$ *is de Rham with jumps $J$* if it is de Rham and the multiplicity at $(\tau', a)$ is $1$ for $a = J(\tau')$ and $0$ otherwise. A character of $D_A$ with values in $\bar{\mathbb{Q}}_l^\times$ is *de Rham at $w$* if it has a de Rham model over some $L' \supseteq L$, and it *has jumps $\{a\}$ at $\tau$* if some de Rham model over some $L'$ has multiplicity $1$ at $a$ and $0$ elsewhere at an embedding $\tau'$ that induces $\tau$. See [de Rham representations](/learn/padic-hodge/#de-rham-representations) in the Background.

**Definition 4.8.3 (Lubin-Tate period property).** The *Lubin-Tate period property* holds if for each prime $l$, each period datum $P$ at $l$ with a tie, each finite extension $K$ of $\mathbb{Q}_l$ and each Lubin-Tate character $\chi$ of $G_K$ that is continuous as a map to $\bar{\mathbb{Q}}_l$, the character $\chi$ has periods in $P$.

### One Lubin-Tate character for each embedding

**Theorem 4.8.4 (Lubin-Tate character at an embedding).** Assume the Lubin-Tate period property. Let $P$ be a period datum at $l$ with a tie, let $w$, $A$ and a local bridge at $A$ that induces $A$ be as above, let $\mathrm{art}$ be a global Artin map, and let $L' \supseteq L$ be a finite extension. Let $j_0 : E_w \to \bar{\mathbb{Q}}_l$ be a continuous ring map. Then there is a homomorphism $\lambda : D_A \to L'^\times$ such that:

1. $\lambda$ is continuous as a map to $\bar{\mathbb{Q}}_l$, and $|\lambda(g)| = 1$ for all $g$;
2. $\lambda$ is de Rham with jumps $J$, where $J(\tau') = -1$ if $\tau'$ induces $j_0|_E$ and $J(\tau') = 0$ otherwise;
3. $\lambda(\sigma) = j_0(x)$ for each unit $x$ of $E_w$ and each $\sigma \in I_A$ with $\mathrm{art}(x) = \sigma^{\mathrm{ab}}$, where $x$ is viewed as an idele at $w$.

Lean: `PositivityTheory.SecR.Hladr.lubinTate_at_embedding`.

*Proof.* There is a Lubin-Tate character $\chi_w$ of $G_{K_w}$ that is continuous and has $|\chi_w(g)| = 1$ for all $g$. The embedding $j_0$ factors as $j_0 = \tau \circ \varphi$, where $\varphi : E_w \to K_w$ is the continuous map that extends $j$ on $E$, and $\tau : K_w \to L'$ is an embedding. An embedding $\tau'$ induces $j_0|_E$ if and only if $\tau' = \tau$. By the Lubin-Tate period property, $\chi_w$ has periods in $P$. For a character with periods, the line $\tau \circ \chi_w$ is de Rham, and its jump at $\tau'$ is $-1$ for $\tau' = \tau$ and $0$ otherwise; this is a separate theorem of the development. The sign comes from the convention $D_{\mathrm{dR}} = (V \otimes B_{\mathrm{dR}})^{G}$: if $y$ is a period in $\mathrm{Fil}^1 \setminus \mathrm{Fil}^2$, then $y^{-1}$ spans the $\tau$-part of $D_{\mathrm{dR}}$ and lies in $\mathrm{Fil}^{-1} \setminus \mathrm{Fil}^0$.

Put $\lambda = \tau \circ \chi_w \circ e$. Then $\lambda$ is continuous, since $e$ and $\chi_w$ are and $\tau$ preserves the absolute value, and $|\lambda(g)| = 1$. The jumps are those of $\tau \circ \chi_w$, which gives 2. For 3, a separate theorem of the development compares the Lubin-Tate character with the global Artin map: for a unit $x$ of $E_w$ and $\sigma \in I_A$ with $\mathrm{art}(x) = \sigma^{\mathrm{ab}}$, we have $\chi_w(e(\sigma)) = \varphi(x)$. So $\lambda(\sigma) = \tau(\varphi(x)) = j_0(x)$. $\square$

### The de Rham property

**Theorem 4.8.5 (de Rham Hecke characters, from Lubin-Tate periods).** Assume the Lubin-Tate period property. Let $E$ be a number field, $l$ a prime, $P$ a period datum at $l$ with a tie, $\iota : \bar{\mathbb{Q}}_l \to \mathbb{C}$ an isomorphism, and $\mathrm{art}$ a global Artin map. Let $\chi$ be an algebraic Hecke character of type $n$ and let $\mu : G_E \to \bar{\mathbb{Q}}_l^\times$ be a continuous homomorphism that is the $l$-adic character of $(\chi, n)$. Let $w$ be a finite place, $A$ a valuation ring of $\Omega$ above $w$, and take a local bridge at $A$ that induces $A$. Then:

1. the restriction of $\mu$ to $D_A$ is de Rham at $w$;
2. for each embedding $\tau : E \to \bar{\mathbb{Q}}_l$ that is induced by an embedding $\tau' : K_w \to L''$ into some finite extension $L''$, the restriction of $\mu$ to $D_A$ has jumps $\{-n(\iota \circ \tau)\}$ at $\tau$.

Lean: `PositivityTheory.SecR.Hladr.field_of_ltPeriods`.

*Proof.* First, a model. There are a finite extension $L' \supseteq L$ and a homomorphism $\psi : D_A \to L'^\times$ that is a model of $\mu|_{D_A}$: its values in $\bar{\mathbb{Q}}_l$ are those of $\mu$. It is continuous and $|\psi(g)| = 1$.

Second, the Lubin-Tate part. The set of continuous embeddings $j : E_w \to \bar{\mathbb{Q}}_l$ is finite. For each $j$ let $\lambda_j$ be given by [the theorem at an embedding](/entry/lubin-tate-at-embedding/), with jump function $J_j$, and put $n_j = n(\iota \circ j|_E)$. Let $\Lambda = \prod_j \lambda_j^{n_j}$. De Rham characters with jumps are closed under products and inverses, and the jumps add. So $\Lambda$ is de Rham with jumps $\sum_j n_j J_j$. Also $\Lambda$ is continuous with $|\Lambda(g)| = 1$.

Third, the finite part. Put $\phi = \psi \Lambda^{-1}$. It is continuous with $|\phi(g)| = 1$. There is an open subgroup $U$ of the units of $E_w$ on which $\chi$ is trivial, and an open subgroup $V$ of $D_A$ such that each $\sigma \in V \cap I_A$ is $\mathrm{art}(x)$ for some $x \in U$. For such $\sigma$ and $x$ the definition of the $l$-adic character gives
$$\mu(\sigma) = \iota^{-1}(\chi(x)) \prod_j j(x)^{n_j} = \prod_j \lambda_j(\sigma)^{n_j} = \Lambda(\sigma),$$
since $\chi(x) = 1$ and $\lambda_j(\sigma) = j(x)$. So $\phi$ is trivial on $V \cap I_A$. A continuous unitary character that is trivial on an open subgroup of inertia is de Rham with all jumps $0$. This is a separate theorem of the development; classically such a character is potentially unramified.

Fourth, the jumps. The product $\psi = \phi\Lambda$ is de Rham with jumps $0 + \sum_j n_j J_j$. This gives 1. For 2, let $\tau$ be induced by $\tau' : K_w \to L''$. Since $L$ contains the images of all embeddings of $K_w$, $\tau'$ gives an embedding $\tau'_1 : K_w \to L'$ that also induces $\tau$. There is exactly one $j_1$ such that $\tau'_1$ induces $j_1|_E$, and then $j_1|_E = \tau$. So $J_{j}(\tau'_1) = -1$ for $j = j_1$ and $0$ for the other $j$, and
$$\sum_j n_j J_j(\tau'_1) = -n_{j_1} = -n(\iota \circ \tau).$$
So the multiplicity at $\tau'_1$ is $1$ at $-n(\iota \circ \tau)$ and $0$ elsewhere. $\square$

**Theorem 4.8.6 (de Rham Hecke characters).** Assume the tilt condition and the product condition of [the previous section](/entry/pre-period/). Then the conclusion of the previous theorem holds for all data as there, where the period datum $P$ has a tie in the form of the published statement.

Lean: `PositivityTheory.SecR.Hladr2.field_of_leaves`.

*Proof.* By [the theorem on periods](/entry/has-periods-main/), the tilt condition and the product condition give the Lubin-Tate period property. The previous theorem then gives the conclusion. $\square$

**Remark 4.8.7 (Formalization).** The published statement `HeckeLAdicCharacterDeRham` at [HeckeLAdicCharacterDeRham.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/HeckeLAdicCharacterDeRham.lean#L11) assumes a tie of type `LocTied`, while `LTPeriods`, the theorem at an embedding and the theorem on periods assume `LocTied6`. These are two structures with the same fields. The proof of the second theorem at [Reduce.lean](lean:Development/WeilBound/CoreStatements/HeckeCharacterDeRham/DeRhamHeckeResults/LAdicHeckeDeRham/LAdicHeckeFields/Reduce.lean#L159) passes one for the other through an instance `CoeTail (Nonempty (LocTied l P AI)) (Nonempty (LocTied6 l P AI))` at [CoeNeTo6.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/LocalComparison/CoeNeTo6.lean#L5), which the source does not show. In the jump clause of the published statement, $L''$ and $\tau'$ appear only in the hypothesis that $\tau$ is induced; the conclusion chooses its own model and embedding. The statement covers every finite place $w$, but a bridge that induces $A$ can exist only if $w$ lies above $l$. The last theorem only joins `field_of_ltPeriods` and `hasPeriods_main`; its caller `field_outright` supplies the two conditions. The model of $\mu$, the comparison of a Lubin-Tate character with the global Artin map, the subgroups $U$ and $V$, and the closure of de Rham characters under products are separate theorems of the development.

## Notes and references

The chapter has two parts. The first part (sections 1 to 6) gives period data and Hodge-Tate data for abelian schemes over $A_{\mathrm{inf}}/(\xi^2)$ and for the formal groups of degenerating abelian schemes, and bounds the colength of the Hodge-Tate periods at split and at unramified places. These results feed the step [every character of the literature](/step/every-character-of-literature/) directly. The second part (sections 7 and 8) proves that the $l$-adic characters of algebraic Hecke characters are de Rham, which [the unconditional form](/entry/field-outright/) uses in the same step.

The period datum is a form of the Hodge-Tate map of a $p$-divisible group over $\mathcal{O}_C$ and of the Weil pairing on its torsion. The Hodge-Tate map and its kernel are due to Tate and, over $\mathcal{O}_C$, to Fargues. The cubical structure on line bundles of abelian schemes is the theorem of the cube. The degeneration data used in the chart forms of the colength bounds are those of Mumford and of Faltings and Chai. The treatment here works at the level of explicit matrices of periods modulo $p^{n+1}$, and the colength bounds are stated for linear data, not for $p$-divisible groups. The Lubin-Tate periods are the classical periods of Lubin-Tate groups in $B_{\mathrm{dR}}^+$, and the de Rham property of Hecke characters is the classical one. Here two steps of the construction of the periods are isolated as the tilt condition and the product condition.

For algebraic Hecke characters of type $A_0$, the existence of the $l$-adic character and its local properties are in Serre, Chapters II and III: the $l$-adic character is locally algebraic, so it is Hodge-Tate at the places above $l$. The de Rham property is the classical form of the last theorems of the chapter. In the classical form the place $w$ lies above $l$ and $\mu$ is restricted to $G_{E_w}$. Here the place is any finite place with a bridge, the local Galois group is the decomposition group $D_A$, carried to $G_{K_w}$ by the bridge, and the result is proved from the tilt condition and the product condition.

- J. Tate, *p-divisible groups*, in: Proceedings of a Conference on Local Fields (Driebergen, 1966), Springer, 1967, §4.
- L. Fargues, *L'isomorphisme entre les tours de Lubin-Tate et de Drinfeld au niveau des points*, in: L'isomorphisme entre les tours de Lubin-Tate et de Drinfeld, Progr. Math. 262, Birkhäuser, 2008.
- D. Mumford, *Abelian Varieties*, Tata Institute Studies in Mathematics 5, Oxford University Press, 1970, §6 and §10.
- D. Mumford, *An analytic construction of degenerating abelian varieties over complete rings*, Compositio Math. 24 (1972), 239-272.
- G. Faltings and C.-L. Chai, *Degeneration of Abelian Varieties*, Ergeb. Math. Grenzgeb. (3) 22, Springer, 1990, Chapters II and III.
- J. Lubin and J. Tate, *Formal complex multiplication in local fields*, Ann. of Math. 81 (1965), 380-387.
- J.-M. Fontaine, *Le corps des périodes p-adiques*, Astérisque 223 (1994), Exposé II.
- J.-P. Serre, *Abelian l-adic Representations and Elliptic Curves*, Benjamin, 1968, Chapters II and III.
